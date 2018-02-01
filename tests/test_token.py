import json
import mock
import unittest
from os import urandom

from ethereum.utils import privtoaddr

from golem_sci.token import GNTWToken, encode_payments
from eth_utils import decode_hex, encode_hex, to_checksum_address


def mock_payment(value: int=1, payee=None):
    p = mock.Mock()
    p.value = value
    p.payee = payee if payee is not None else urandom(20)
    return p


def abi_encoder(function_name, args):
    def bytes2hex(elem):
        if isinstance(elem, bytes):
            return encode_hex(elem)
        if isinstance(elem, list):
            for i, e in enumerate(elem):
                elem[i] = bytes2hex(e)
        return elem

    args = bytes2hex(args.copy())
    res = json.dumps({'function_name': function_name, 'args': args})
    return res


class GNTWTokenTest(unittest.TestCase):
    def setUp(self):
        self.client = mock.Mock()
        self.privkey = urandom(32)
        self.addr = encode_hex(privtoaddr(self.privkey))
        self.token = GNTWToken(self.client)

        gnt_abi = mock.Mock()
        gnt_abi.encode_function_call.side_effect = abi_encoder
        self.token._gnt = gnt_abi

        gntw_abi = mock.Mock()
        gntw_abi.encode_function_call.side_effect = abi_encoder
        self.token._gntw = gntw_abi

        self.balances = {
            'gnt': None,
            'gntw': None,
        }

        self.pda = bytearray(32)
        self.pda_create_called = False

        def client_call(_from, to, data, block):
            self.assertEqual('pending', block)
            token_addr = to
            data = json.loads(decode_hex(data).decode())
            if data['function_name'] == 'balanceOf':
                self.assertEqual(1, len(data['args']))

                if privtoaddr(self.privkey) == decode_hex(data['args'][0]):
                    if token_addr == self.token.TESTGNT_ADDRESS:
                        return self.balances['gnt']
                    if token_addr == self.token.GNTW_ADDRESS:
                        return self.balances['gntw']

                raise Exception('Unknown balance')

            if data['function_name'] == 'getPersonalDepositAddress':
                self.assertEqual(self.token.GNTW_ADDRESS, token_addr)
                self.assertEqual(1, len(data['args']))
                self.assertEqual(
                    privtoaddr(self.privkey),
                    decode_hex(data['args'][0]))
                return encode_hex(self.pda)

            raise Exception('Unknown call {}'.format(data['function_name']))

        self.nonce = 0
        self.process_deposit_called = False
        self.transfer_called = False

        def client_send(tx):
            token_addr = to_checksum_address(encode_hex(tx.to))
            data = json.loads(tx.data)
            self.assertEqual(self.nonce, tx.nonce)
            self.nonce += 1
            if data['function_name'] == 'createPersonalDepositAddress':
                self.assertEqual(self.token.GNTW_ADDRESS, token_addr)
                self.assertEqual(0, len(data['args']))
                self.assertEqual(
                    self.token.CREATE_PERSONAL_DEPOSIT_GAS,
                    tx.startgas)
                self.pda_create_called = True
                return encode_hex(urandom(32))

            if data['function_name'] == 'transfer':
                self.assertEqual(self.token.TESTGNT_ADDRESS, token_addr)
                self.assertEqual(2, len(data['args']))
                self.assertEqual(encode_hex(self.pda[-20:]), data['args'][0])
                self.assertEqual(int(self.balances['gnt'], 16), data['args'][1])
                self.transfer_called = True
                return encode_hex(urandom(32))

            if data['function_name'] == 'processDeposit':
                self.assertEqual(self.token.GNTW_ADDRESS, token_addr)
                self.assertEqual(0, len(data['args']))
                self.process_deposit_called = True
                return encode_hex(urandom(32))

            raise Exception('Unknown send {}'.format(data['function_name']))

        self.client.call.side_effect = client_call
        self.client.send.side_effect = client_send
        self.client.get_transaction_count.side_effect = lambda *_: self.nonce

    def test_get_balance(self):
        self.assertEqual(None, self.token.get_balance(self.addr))

        self.balances['gnt'] = '0x'
        self.assertEqual(None, self.token.get_balance(self.addr))

        self.balances['gntw'] = '0x'
        self.assertEqual(0, self.token.get_balance(self.addr))

        self.balances['gnt'] = '0xf'
        self.assertEqual(15, self.token.get_balance(self.addr))

        self.balances['gntw'] = '0xa'
        self.assertEqual(25, self.token.get_balance(self.addr))

    def test_batches_enough_gntw(self):
        p1 = mock_payment(1)
        p2 = mock_payment(2)
        p3 = mock_payment(3)

        self.balances['gnt'] = '0x0'
        self.balances['gntw'] = '0xf'

        closure_time = 0
        tx = self.token.batch_transfer(self.privkey, [p1, p2, p3], closure_time)
        self.assertEqual(self.nonce, tx.nonce)
        self.assertEqual(
            self.token.GNTW_ADDRESS,
            to_checksum_address(encode_hex(tx.to)),
        )
        self.assertEqual(0, tx.value)
        expected_gas = self.token.GAS_BATCH_PAYMENT_BASE + \
            3 * self.token.GAS_PER_PAYMENT
        self.assertEqual(expected_gas, tx.startgas)
        expected_data = abi_encoder(
            'batchTransfer',
            [encode_payments([p1, p2, p3]), closure_time])
        self.assertEqual(expected_data, tx.data)

    def test_batches_gnt_convertion(self):
        p1 = mock_payment()

        self.balances['gnt'] = '0x10'
        self.balances['gntw'] = '0x0'

        # Will need to convert GNT to GNTW
        closure_time = 0
        tx = self.token.batch_transfer(self.privkey, [p1], closure_time)
        self.assertEqual(None, tx)
        # Created personal deposit
        self.assertTrue(self.pda_create_called)
        self.pda_create_called = False
        # Waiting for personal deposit tx to be mined
        tx = self.token.batch_transfer(self.privkey, [p1], closure_time)
        self.assertEqual(None, tx)
        self.assertFalse(self.pda_create_called)
        self.assertFalse(self.transfer_called)
        self.assertFalse(self.process_deposit_called)
        # Personal deposit tx mined, sending and processing deposit
        self.pda = urandom(32)
        tx = self.token.batch_transfer(self.privkey, [p1], closure_time)
        self.assertEqual(None, tx)
        # 2 transactions to convert GNT to GNTW
        self.assertEqual(3, self.nonce)
        self.assertTrue(self.transfer_called)
        self.assertTrue(self.process_deposit_called)

    def test_payment_aggregation(self):
        a1 = urandom(20)
        a2 = urandom(20)
        a3 = urandom(20)

        self.balances['gnt'] = '0x0'
        self.balances['gntw'] = '0xf'

        payments = [
            mock_payment(payee=a1),
            mock_payment(payee=a2),
            mock_payment(payee=a2),
            mock_payment(payee=a3),
            mock_payment(payee=a3),
            mock_payment(payee=a3),
        ]

        closure_time = 0
        tx = self.token.batch_transfer(self.privkey, payments, closure_time)

        expected_gas = self.token.GAS_BATCH_PAYMENT_BASE + \
            3 * self.token.GAS_PER_PAYMENT
        data = json.loads(tx.data)
        self.assertEqual(3, len(data['args'][0]))
        self.assertEqual(expected_gas, tx.startgas)
