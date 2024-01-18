import pandas as pd
import numpy as np
from src.DimondPricePrediction.logger import logging
from sklearn.model_selection import train_test_split
from src.DimondPricePrediction.exception import customexception 
from dataclasses import dataclass
from pathlib import path 

class DataInjection:
    def __init__(self):
        pass
    
    def initiate_data_injection(self):
        logging.info("Data injection started")
        
        try:
            data = pd.read_csv(Path(os.path.join("notebooks/data","train.csv")))
            logging.info("read the data set as data frame ")
            
            
            logging.info("I have now performed train test split")
            
            train_data,test_data = train_test_split(data,test_size=0.25) 
            logging,info("train test split completed")
            
               