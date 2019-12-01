import re
from vowpalwabbit import pyvw
from nltk.corpus import stopwords
from flask import Flask, jsonify, request

# Carregar o modelo

class Classifier:
    def __init__(self):
        self.vw = pyvw.vw("-i imdb.model")
    
    def cleanData(self, sentence):

        stopWords = stopwords.words('english')
        processedList = ""
    
        #convert to lowercase and ignore special charcter
        sentence = re.sub(r'[^A-Za-z0-9\s.]', r'', str(sentence).lower())
        sentence = re.sub(r'\n', r' ', sentence)
        
        sentence = " ".join([word for word in sentence.split() if word not in stopWords])
        return sentence

    def to_vw_format(self, document, label=None):
      return str(label) + ' |text ' + document
    
    def train(self, train, label):
        vw_text = self.to_vw_format(train, 1 if label == 1 else -1)
        self.vw.learn(vw_text)