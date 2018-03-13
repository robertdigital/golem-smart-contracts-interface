ADDRESS = '0x54fe0c9b4860b7ce43a7e191f81b6c6fad3efc06'
ABI = '[{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_subtask_id","type":"bytes32"}],"name":"reimburseForVerificationCosts","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balances","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"coldwallet","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"isUnlocked","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"concent","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"isLocked","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"}],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_whom","type":"address"},{"name":"_burn","type":"uint256"}],"name":"burn","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"unlock","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"isTimeLocked","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_requestor","type":"address"},{"name":"_provider","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_subtask_id","type":"bytes32"}],"name":"reimburseForSubtask","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_amount","type":"uint256"},{"name":"","type":"bytes"}],"name":"onTokenReceived","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"getTimelock","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"locked_until","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"withdrawal_delay","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"lock","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"token","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_requestor","type":"address"},{"name":"_provider","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_closure_time","type":"uint256"}],"name":"reimburseForNoPayment","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"_token","type":"address"},{"name":"_concent","type":"address"},{"name":"_coldwallet","type":"address"},{"name":"_withdrawal_delay","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":false,"name":"_amount","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_amount","type":"uint256"}],"name":"Withdraw","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"}],"name":"Lock","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"}],"name":"Unlock","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_who","type":"address"},{"indexed":false,"name":"_amount","type":"uint256"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_requestor","type":"address"},{"indexed":true,"name":"_provider","type":"address"},{"indexed":false,"name":"_amount","type":"uint256"},{"indexed":false,"name":"_subtask_id","type":"bytes32"}],"name":"ReimburseForSubtask","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_requestor","type":"address"},{"indexed":true,"name":"_provider","type":"address"},{"indexed":false,"name":"_amount","type":"uint256"},{"indexed":false,"name":"_closure_time","type":"uint256"}],"name":"ReimburseForNoPayment","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":false,"name":"_amount","type":"uint256"},{"indexed":false,"name":"_subtask_id","type":"bytes32"}],"name":"ReimburseForVerificationCosts","type":"event"}]'  # noqa
BIN = '6060604052341561000f57600080fd5b6040516080806114328339810160405280805190602001909190805190602001909190805190602001909190805190602001909190505083600360006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550826000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555081600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055508060028190555050505050611310806101226000396000f300606060405260043610610107576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806327dcecdb1461010c57806327e235e31461015b5780632812d4a7146101a85780632bbf532a146101fd57806341b98c761461024e5780634a4fbeec146102a357806351cff8d9146102f457806370a082311461032d5780639dc29fac1461037a578063a69df4b5146103bc578063b8cc2751146103d1578063ba4c946914610422578063bed2554214610490578063bf1e799b14610515578063c8c36d9114610562578063eaa26f0f146105af578063f83d08ba146105d8578063fc0c546a146105ed578063fc32339a14610642575b600080fd5b341561011757600080fd5b610159600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091908035906020019091908035600019169060200190919050506106ac565b005b341561016657600080fd5b610192600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091905050610797565b6040518082815260200191505060405180910390f35b34156101b357600080fd5b6101bb6107af565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b341561020857600080fd5b610234600480803573ffffffffffffffffffffffffffffffffffffffff169060200190919050506107d5565b604051808215151515815260200191505060405180910390f35b341561025957600080fd5b61026161086b565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b34156102ae57600080fd5b6102da600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091905050610890565b604051808215151515815260200191505060405180910390f35b34156102ff57600080fd5b61032b600480803573ffffffffffffffffffffffffffffffffffffffff169060200190919050506108db565b005b341561033857600080fd5b610364600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091905050610b19565b6040518082815260200191505060405180910390f35b341561038557600080fd5b6103ba600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091908035906020019091905050610b62565b005b34156103c757600080fd5b6103cf610c1e565b005b34156103dc57600080fd5b610408600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091905050610cab565b604051808215151515815260200191505060405180910390f35b341561042d57600080fd5b61048e600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190803573ffffffffffffffffffffffffffffffffffffffff1690602001909190803590602001909190803560001916906020019091905050610cf6565b005b341561049b57600080fd5b610513600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190803590602001909190803590602001908201803590602001908080601f01602080910402602001604051908101604052809392919081815260200183838082843782019150505050505091905050610dd7565b005b341561052057600080fd5b61054c600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091905050610ed3565b6040518082815260200191505060405180910390f35b341561056d57600080fd5b610599600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091905050610f1c565b6040518082815260200191505060405180910390f35b34156105ba57600080fd5b6105c2610f34565b6040518082815260200191505060405180910390f35b34156105e357600080fd5b6105eb610f3a565b005b34156105f857600080fd5b610600610fc4565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b341561064d57600080fd5b6106aa600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190803573ffffffffffffffffffffffffffffffffffffffff16906020019091908035906020019091908035906020019091905050610fea565b005b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614151561070757600080fd5b61073483600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16846110c3565b8273ffffffffffffffffffffffffffffffffffffffff167fd87ab4af3bd64a3a6c4b8396a3a2aaad6419190934db64d5b7be20a81a5eaab183836040518083815260200182600019166000191681526020019250505060405180910390a2505050565b60046020528060005260406000206000915090505481565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b600080600560008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205414158015610864575042600560008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054105b9050919050565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b600080600560008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054149050919050565b60006108e6336107d5565b15156108f157600080fd5b600460003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205490506000600460003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055506000600560003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002081905550600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1663a9059cbb83836000604051602001526040518363ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200182815260200192505050602060405180830381600087803b1515610a8a57600080fd5b6102c65a03f11515610a9b57600080fd5b505050604051805190501515610ab057600080fd5b8173ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff167f9b1bfa7fa9ee420a16e124f794c35ac9f90472acc99140eb2f6447c714cad8eb836040518082815260200191505060405180910390a35050565b6000600460008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549050919050565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16141515610bbd57600080fd5b610bcc8263deadbeef836110c3565b8173ffffffffffffffffffffffffffffffffffffffff167fcc16f5dbb4873280815c1ee09dbd06736cffcc184412cf7a71a0fdb75d397ca5826040518082815260200191505060405180910390a25050565b6002544201600560003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055503373ffffffffffffffffffffffffffffffffffffffff167f0be774851955c26a1d6a32b13b020663a069006b4a3b643ff0b809d31826057260405160405180910390a2565b600042600560008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054119050919050565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16141515610d5157600080fd5b610d5c8484846110c3565b8273ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff167f5e73339b88b13a2882423746a5db6cbef7a80b5cfc43dfeaf6a54ff944f6a99884846040518083815260200182600019166000191681526020019250505060405180910390a350505050565b600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16141515610e3357600080fd5b81600460008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825401925050819055508273ffffffffffffffffffffffffffffffffffffffff167fe1fffcc4923d04b559f4d29a8bfc6cda04eb5b0d3c460751c2402c5c5cc9109c836040518082815260200191505060405180910390a2505050565b6000600560008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549050919050565b60056020528060005260406000206000915090505481565b60025481565b6000600560003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055503373ffffffffffffffffffffffffffffffffffffffff167fc1b5f12cea7c200ad495a43bf2d4c7ba1a753343c06c339093937849de84d91360405160405180910390a2565b600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614151561104557600080fd5b6110508484846110c3565b8273ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff167f6433c762be670c059832a954094d4df564def570aeb0e06ccd4afc421e4a28e98484604051808381526020018281526020019250505060405180910390a350505050565b80600460008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020541015151561111157600080fd5b80600460008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825403925050819055506000600460008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205414156111ec576000600560008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055505b600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1663a9059cbb83836000604051602001526040518363ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200182815260200192505050602060405180830381600087803b15156112b957600080fd5b6102c65a03f115156112ca57600080fd5b5050506040518051905015156112df57600080fd5b5050505600a165627a7a7230582029f1f8a61bec0298c6bd479b76a33a8451f53b600e9466812338c93e9958e6e60029'  # noqa
