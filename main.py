from sensor.exception import SensorException
from sensor.logger import logging
import sys,os
from sensor.utils import get_collection_as_dataframe
from sensor.entity import config_entity
from sensor.components import data_ingestion
from sensor.entity import artifact_entity
from sensor import utils
from sensor.components.data_ingestion import DataIngestion


def test_logger_and_exception():
    try:
        logging.info("starting test logger_exception")
        a=2/0
        print(a)
        logging.info("executing")
    except Exception as e:
        raise SensorException(e,sys)

    
if __name__ == "__main__":
    try:
        training_pipeline_config = config_entity.TrainingPipelineConfig()
        data_ingestion_config= config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        print(data_ingestion_config.to_dict())
        data_ingestion= DataIngestion(data_ingestion_config=data_ingestion_config)
        print(data_ingestion.initiate_data_ingestion())
    except Exception as e:
        print(e)
    