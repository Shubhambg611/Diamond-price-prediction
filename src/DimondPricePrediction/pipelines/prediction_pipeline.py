#4nov   
import os 
import sys 
import pandas as pd 
import numpy as np
from src.DimondPricePrediction.logger import logging 
from src.DimondPricePrediction.exception import customexception 
from src.DimondPricePrediction.utils.utils import load_object  

class PredictPipeline:
    def __init__(self):
        pass
    def predict(self,features):
        try:
            #load data
            preprocessor_path = os.path.join('artifact','preprocessor.pkl')
            model_path = os.path.join('artifact','model.pkl')

            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)
            
            #transform data
            scaled_data = preprocessor.transform(features)
            pred = model.predict(scaled_data)
            
            return pred
            
            
            
            
            
        except Exception as e:
            raise customexception(e,sys)
        
         