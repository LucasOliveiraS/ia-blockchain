from web3 import Web3

web3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/9fe6f0a016494dfeb4cecd7d1c98431a"))

from web3.middleware import geth_poa_middleware

web3.middleware_onion.inject(geth_poa_middleware, layer=0)

abi = '''
    [
	{
		"constant": false,
		"inputs": [],
		"name": "getData",
		"outputs": [
			{
				"name": "data",
				"type": "int256[][]"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "msgSender",
				"type": "address"
			},
			{
				"name": "data",
				"type": "int256[]"
			}
		],
		"name": "handleAddData",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "data",
				"type": "int256[][]"
			},
			{
				"name": "newData",
				"type": "int256[]"
			}
		],
		"name": "isDataEqual",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "transferOwnership",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "",
				"type": "bytes32"
			}
		],
		"name": "addedData",
		"outputs": [
			{
				"name": "t",
				"type": "uint256"
			},
			{
				"name": "sender",
				"type": "address"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"name": "",
				"type": "address"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "",
				"type": "uint256"
			},
			{
				"name": "",
				"type": "uint256"
			}
		],
		"name": "publicData",
		"outputs": [
			{
				"name": "",
				"type": "int256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	}
]
      '''

address = Web3.toChecksumAddress('0xA842b77e6D4A57fae2A3ED44F68978111dC8bDeF')      
lucas = '0x690809206b73994282910F1740a729a89aF4beCa'

myContract = web3.eth.contract(address=address, abi=abi)

key = myContract.functions.receive_data([2,9]).buildTransaction({'nonce': web3.eth.getTransactionCount(lucas)})
signed_tx = web3.eth.account.signTransaction(key, private_key='8714f19637f79f8cdec1d994184ace4dda3984256f207147abee84a065f43941')
web3.eth.sendRawTransaction(signed_tx.rawTransaction)

#addedData = myContract.functions.getData().call()
#print(addedData)