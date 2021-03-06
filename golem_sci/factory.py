import logging
import re
import time
from typing import Callable, Dict

from distutils.version import StrictVersion

# this must be before any other ethereum imports
from . import fix_logging
from ethereum.transactions import Transaction
from web3 import Web3, IPCProvider, HTTPProvider
from web3.middleware import geth_poa_middleware

from . import chains, contracts
from .client import Client
from .implementation import SCIImplementation
from .interface import SmartContractsInterface
from .transactionsstorage import TransactionsStorage

logger = logging.getLogger(__name__)


GENESES = {
    chains.MAINNET:
        '0xd4e56740f876aef8c010b86a40d5f56745a118d0906a34e69aec8c0db1cb8fa3',
    chains.RINKEBY:
        '0x6341fd3daf94b748c72ced5a5b26028f2474f5f00d824504e4fa37a75767e177',
}

MIN_GETH_VERSION = StrictVersion('1.7.2')
MAX_GETH_VERSION = StrictVersion('1.9.999')


def new_sci_ipc(
        ipc: str,
        address: str,
        chain: str,
        storage: TransactionsStorage,
        contract_addresses: Dict[contracts.Contract, str],
        tx_sign: Callable[[Transaction], None]=None) -> SmartContractsInterface:
    return new_sci(
        Web3(IPCProvider(ipc)),
        address,
        chain,
        storage,
        contract_addresses,
        tx_sign,
    )


def new_sci_rpc(
        rpc: str,
        address: str,
        chain: str,
        storage: TransactionsStorage,
        contract_addresses: Dict[contracts.Contract, str],
        tx_sign: Callable[[Transaction], None]=None) -> SmartContractsInterface:
    return new_sci(
        Web3(HTTPProvider(rpc)),
        address,
        chain,
        storage,
        contract_addresses,
        tx_sign,
    )


def new_sci(
        web3: Web3,
        address: str,
        chain: str,
        storage: TransactionsStorage,
        contract_addresses: Dict[contracts.Contract, str],
        tx_sign: Callable[[Transaction], None]=None) -> SmartContractsInterface:
    # Web3 needs this extra middleware to properly handle rinkeby chain because
    # rinkeby is POA which violates some invariants
    if chain == chains.RINKEBY and \
            geth_poa_middleware not in web3.middleware_stack:
        web3.middleware_stack.inject(geth_poa_middleware, layer=0)
    _ensure_connection(web3)
    _ensure_geth_version(web3)
    _ensure_genesis(web3, chain)
    geth_client = Client(web3)
    return SCIImplementation(
        geth_client,
        address,
        storage,
        contract_addresses,
        tx_sign,
    )


def _ensure_genesis(web3: Web3, chain: str):
    genesis_hash = web3.eth.getBlock(0)['hash'].hex()
    if genesis_hash != GENESES[chain]:
        raise Exception(
            'Invalid genesis block for {}, expected {}, got {}'.format(
                chain,
                GENESES[chain],
                genesis_hash,
            )
        )


def _ensure_connection(web3: Web3):
    RETRY_COUNT = 10
    for _ in range(RETRY_COUNT):
        if web3.isConnected():
            return
        time.sleep(1)
    raise Exception('Could not connect to geth: {}'.format(web3.providers))


def _ensure_geth_version(web3: Web3):
    version = web3.version.node.split('/')
    if version[0] != 'Geth':
        raise Exception('Expected geth client, got {}'.format(version[0]))
    matches = re.search('^v(\d+\.\d+\.\d+)', version[1])
    if matches is None:
        raise Exception('Malformed version string: {}'.format(version[1]))
    match = matches.group(1)

    ver = StrictVersion(match)
    logger.info('Geth version: %s', ver)
    if ver < MIN_GETH_VERSION or ver > MAX_GETH_VERSION:
        raise Exception(
            'Incompatible geth version: {}. Expected >= {} and <= {}'.format(
                ver,
                MIN_GETH_VERSION,
                MAX_GETH_VERSION,
            ))
