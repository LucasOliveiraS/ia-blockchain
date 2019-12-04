import re
import pandas as pd
from sklearn.metrics import confusion_matrix
from vowpalwabbit import pyvw
from nltk.corpus import stopwords
from flask import Flask, jsonify, request

class Classifier:
    def __init__(self):
        self.vw = pyvw.vw("-i model/imdb2.model")
        self.valid = self.loadValidData()
        self.accuracy = self.getAccuracy()
    
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

    def loadValidData(self):
        valid = pd.read_csv('app/test_data/imdb_data_valid.csv')
        del valid['Unnamed: 0']
        return valid

    def evaluation(self):

        for index, row in self.valid.iterrows():
            vw_text_valid = self.to_vw_format(row['processed_reviews'])
            self.valid['probability'].loc[index] = self.vw.predict(vw_text_valid)

        self.valid.loc[self.valid.probability > 0, 'prediction'] = True
        self.valid.loc[self.valid.probability < 0, 'prediction'] = False
        self.valid["truth"] = self.valid.label==1

        return ((self.valid.truth==self.valid.prediction).mean())

    def getAccuracy(self):
        return ((self.valid.truth==self.valid.prediction).mean())

    def compareAccuracy(self, new_accuracy):
        if(new_accuracy > self.accuracy):
            return True
        else:
            return False