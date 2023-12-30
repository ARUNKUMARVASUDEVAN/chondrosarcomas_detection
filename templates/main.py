from chondrosarcomas_detection import logger
from chondrosarcomas_detection.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from chondrosarcomas_detection.pipeline.stage_02_base_model import PrepareBaseModelTrainingPipeline
from chondrosarcomas_detection.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from chondrosarcomas_detection.pipeline.stage_04_model_evaluation_mlflow import EvaluationPipeline
from pathlib import Path

STAGE_NAME="Data Ingestion stage"

try:
        logger.info(f">>>>> stage {STAGE_NAME} started<<<<<<")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nX===========X")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME ="PREPARE base model"

if __name__ == "__main__":
    try:
        logger.info(f"***********")
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj=PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\n x==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME="Training"


if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
        
STAGE_NAME = "Evaluation stage"

if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e