import seaborn as sns
import numpy as np
import pandas as pd
import pickle
from keras.models import model_from_json
from sklearn.preprocessing import StandardScaler

class predic():
    
    
    def __init__(self, pathjs = 'lstm_model.json', path_weights='lstm_model.h5', dataFit='dataFit.csv'):
        self.model = self.load_model(pathjs, path_weights)
        self.scaler = StandardScaler()
        data = pd.read_csv(dataFit)
        self.scaler.fit(data.drop(["Label"], axis=1))
 #------   
 
    def Transform_data(self,newList):
        X = self.scaler.transform(newList)
        return X
#------

    def load_model(self,pathjs, path_weights):
        # loading model
        model = model_from_json(open(pathjs).read())
        model.load_weights(path_weights)
        model.compile(loss='categorical_crossentropy', optimizer='adam')
        return model
#------
# function to take the data (1. send it to transform 2. send it to prediction 3. return the preduction)   

    def predctionVal (self, newList):
        # convert NaN values to 0.0
        new = np.array(newList)
        new[np.isnan(new)] = 0.0
        newList = new
        # transform the data using the scaler
        X = self.Transform_data(newList)
        # make a prediction using the model
        pred = self.model.predict(X)
        pred1 = np.argmax(pred, axis=1)
        # encoding
        label_dict= {0:'CALM', 1:'GOOD-MOOD', 2:'STRESSED'}
        prediction = label_dict[int(pred1)]
        return prediction
        
        
        
        

        
        
        