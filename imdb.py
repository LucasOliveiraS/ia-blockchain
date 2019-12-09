import re
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from vowpalwabbit import pyvw
from nltk.corpus import stopwords
from flask import Flask, jsonify, request
from sklearn.model_selection import KFold

class Classifier:
    def __init__(self):
        self.vw = pyvw.vw("-i model/imdb2.model")
        self.valid = self.loadValidData()
        self.accuracy = self.evaluation()
    
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

        X = self.valid['processed_reviews']
        y = self.valid['label']

        scores = []

        cv = KFold(n_splits=5, random_state=42, shuffle=False)
        for train_index, test_index in cv.split(X):
            
            probability = []
            
            X_train, X_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]
            for index in X_test.iteritems():
                vw_text_valid = self.to_vw_format(index[1])
                probability.append(self.vw.predict(vw_text_valid))
                
            # Calcula acurácia
            valid_data = pd.DataFrame(probability, columns=['probability'])
            valid_data.loc[valid_data.probability > 0, 'prediction'] = True
            valid_data.loc[valid_data.probability < 0, 'prediction'] = False
            valid_data['truth'] = np.where(y_test==1, True, False)
            
            scores.append((valid_data.truth==valid_data.prediction).mean())

        accuracy_mean = sum(scores) / len(scores)
        return accuracy_mean

    def getAccuracy(self):
        return ((self.valid.truth==self.valid.prediction).mean())

    def compareAccuracy(self, new_accuracy):
        if(new_accuracy > self.accuracy):
            return True
        else:
            return False