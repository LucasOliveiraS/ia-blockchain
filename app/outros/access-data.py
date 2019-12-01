from web3 import Web3

web3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/9fe6f0a016494dfeb4cecd7d1c98431a"))

from web3.middleware import geth_poa_middleware

web3.middleware_onion.inject(geth_poa_middleware, layer=0)

web3.eth.defaultAddress = '0x690809206b73994282910F1740a729a89aF4beCa'

print(web3.eth.blockNumber)

x = web3.isAddress('0xacb0ceacb13e786644f0ab21aa044032ae925874')
print(x)

abi = '''
    [
	{
		"constant": false,
		"inputs": [
			{
				"name": "key",
				"type": "uint256"
			}
		],
		"name": "getData",
		"outputs": [
			{
				"name": "d",
				"type": "int64[]"
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
				"name": "data",
				"type": "int64[]"
			}
		],
		"name": "storeData",
		"outputs": [
			{
				"name": "key",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "",
				"type": "uint256"
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
	}
]
'''

address = Web3.toChecksumAddress('0xacb0ceacb13e786644f0ab21aa044032ae925874')
lucas = '0x690809206b73994282910F1740a729a89aF4beCa'

myContract = web3.eth.contract(address=address, abi=abi)
#key = myContract.functions.storeData([1,4]).transact()
key = myContract.functions.storeData([1,4]).buildTransaction({'nonce': web3.eth.getTransactionCount(lucas)})
signed_tx = web3.eth.account.signTransaction(key, private_key='8714f19637f79f8cdec1d994184ace4dda3984256f207147abee84a065f43941')
web3.eth.sendRawTransaction(signed_tx.rawTransaction)


addedData = myContract.functions.getData(key).call()
print(addedData)