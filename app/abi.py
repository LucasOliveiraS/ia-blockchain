class Abi:
    def __init__(self):
        self.abi = '''
    [
	{
		"constant": false,
		"inputs": [
			{
				"internalType": "bytes32",
				"name": "key",
				"type": "bytes32"
			}
		],
		"name": "accessData",
		"outputs": [
			{
				"internalType": "string",
				"name": "feature",
				"type": "string"
			},
			{
				"internalType": "int256",
				"name": "label",
				"type": "int256"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [],
		"name": "getData",
		"outputs": [
			{
				"internalType": "string[]",
				"name": "feature",
				"type": "string[]"
			},
			{
				"internalType": "int256[]",
				"name": "label",
				"type": "int256[]"
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
				"internalType": "address",
				"name": "msgSender",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "feature",
				"type": "string"
			},
			{
				"internalType": "int256",
				"name": "label",
				"type": "int256"
			}
		],
		"name": "handleAddData",
		"outputs": [
			{
				"internalType": "bytes32",
				"name": "key",
				"type": "bytes32"
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
				"internalType": "string",
				"name": "newData",
				"type": "string"
			}
		],
		"name": "isDataEqual",
		"outputs": [
			{
				"internalType": "bool",
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
				"internalType": "address",
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
				"internalType": "bytes32",
				"name": "",
				"type": "bytes32"
			}
		],
		"name": "addedData",
		"outputs": [
			{
				"internalType": "string",
				"name": "feature",
				"type": "string"
			},
			{
				"internalType": "int256",
				"name": "label",
				"type": "int256"
			},
			{
				"internalType": "uint256",
				"name": "t",
				"type": "uint256"
			},
			{
				"internalType": "address",
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
		"name": "getLength",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
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
				"internalType": "address",
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
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "publicFeature",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
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
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "publicLabel",
		"outputs": [
			{
				"internalType": "int256",
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

    def getAbi(self):
        return self.abi