from web3 import Web3
from flask import Flask, jsonify, request
import sys
sys.path.insert(1, '/home/lucas/Documents/Projetos/Blockchain/Data Storage')
from imdb import Classifier
from abi import Abi

web3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/9fe6f0a016494dfeb4cecd7d1c98431a"))

from web3.middleware import geth_poa_middleware

web3.middleware_onion.inject(geth_poa_middleware, layer=0)

class Contract:

	def __init__(self):
		self.address = ''
		self.address_contract = Web3.toChecksumAddress('0xFeDDD6C2E2dA7c1C64D1785d7d38b269Dd971478')

	def connectContract(self, abi):
		myContract = web3.eth.contract(address=self.address_contract, abi=abi)
		return myContract

	def addData(self, train, label, gas = 420000):
		return train, label, gas

	def displayData(self, connection):
		addedData = connection.functions.getData().call()
		return addedData
	
	def getAddress(self, address):
		self.address = Web3.toChecksumAddress(address)

# Creating a Web App
app = Flask(__name__)

contract = Contract()
classifier = Classifier()

abi = Abi()
connection = contract.connectContract(abi.getAbi())

@app.route('/get_data', methods = ['GET'])
def getData():
	response = {'data' : len(contract.displayData(connection)[0])}
	return jsonify(response), 200

@app.route('/get_accuracy', methods = ['GET'])
def getAccuracy():
	accuracy = round(classifier.accuracy, 2)
	accuracy_s = str(accuracy)

	response = {'accuracy' : accuracy_s}
	return jsonify(response), 200

# Adicionando dados
@app.route('/add_data', methods = ['POST'])
def transact():
		receive = request.get_json()

		train = classifier.cleanData(receive['train'])
		label = int(receive['label'])

		train, label, gas = contract.addData(train, label, 420000)
		classifier.train(train, label)

		new_accuracy = classifier.evaluation()
		payment = classifier.compareAccuracy(new_accuracy)

		print("Current accuracy: ", classifier.accuracy)
		print("New accuracy: ", new_accuracy)

		if(payment == True):
			key = connection.functions.handleAddData(contract.address, train, label).buildTransaction({'nonce': web3.eth.getTransactionCount(contract.address), 'gas': gas})
			signed_tx = web3.eth.account.signTransaction(key, private_key='YOUR KEY')
			web3.eth.sendRawTransaction(signed_tx.rawTransaction)

			response = {'message' : 'True', 'new_accuracy' : new_accuracy, 'last_accuracy' : classifier.accuracy}
			classifier.accuracy = new_accuracy
		else:
			response = {'message' : 'False'}

		return response, 201

@app.route('/predict', methods = ['POST'])
def predict():
	receive = request.get_json()
	input = classifier.cleanData(receive['input'])

	predict = classifier.vw.predict(' |text ' + input)

	if(predict > 0):
		response = {'output' : 'Good'}
	elif(predict < 0):
		response = {'output' : 'Bad'}
	
	return jsonify(response), 200

@app.route('/address', methods = ['POST'])
def getAdress():
	receive = request.get_json()
	print('Address: ', receive)
	contract.getAddress(receive)
	response = {'address' : 'Address ok'}
	return jsonify(response), 200

app.run(host='localhost', port=5000)