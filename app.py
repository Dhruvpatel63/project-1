from src.project1.logger import logging
from src.project1.exception import CustomException
from src.project1.components.data_ingestion import DataIngestion
from src.project1.components.data_ingestion import DataIngestionConfig
from src.project1.components.data_transformation import DataTransformationConfig,DataTransformation
import sys

if __name__=="__main__":
    logging.info("The execution has started")


    try:
        data_ingestion=DataIngestion()
        # data_ingestion.initiate_data_ingestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        # data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        data_transformation.initiate_data_transformation(train_data_path,test_data_path)


    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)