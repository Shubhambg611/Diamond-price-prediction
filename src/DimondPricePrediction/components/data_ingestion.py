import pandas as pd
import numpy as np
from src.DimondPricePrediction.logger import logging
from sklearn.model_selection import train_test_split
from src.DimondPricePrediction.exception import customexception 
from dataclasses import dataclass
from pathlib import path 

class DataIngestionConfig:
    raw_data_path: str=os.path.join("artifact","raw.csv")
    train_data_path: str=os.path.join("artifacts","train.csv")
    test_data_path: str=os.path.join("artifacts","test.csv")

class DataIngestion:
    def __init__(self):
        self.injection_config=DataIngestionConfig()
    
    def initiate_data_injection(self):
        logging.info("Data injection started")
        
        try:
            data = pd.read_csv(Path(os.path.join("notebooks/data","train.csv")))
            logging.info("read the data set as data frame ")
            
            os.makedirs(os.path.join(self.ingestion_config.raw_data_path),exists=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("I have saved the raw data in artifact folder")
            
            
            logging.info("I have now performed train test split")
            
            train_data,test_data = train_test_split(data,test_size=0.25) 
            logging,info("train test split completed")  
            
            
            
        except Expetion as e:
            pass
        