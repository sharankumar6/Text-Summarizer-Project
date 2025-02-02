from src.TextSummarizer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from src.TextSummarizer.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from src.TextSummarizer.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline
from src.TextSummarizer.pipeline.stage_04_model_training import ModelTrainingPipeline
from src.TextSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
from TextSummarizer.logging import logger


# Data Ingestion
STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>>>>>>> Stage: {STAGE_NAME} Started <<<<<<<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>>>>> Stage: {STAGE_NAME} Completed <<<<<<<<<<<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e


# Data Validation
STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>>>>>>>>> Stage: {STAGE_NAME} Started <<<<<<<<<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>>>>>> Stage: {STAGE_NAME} Completed <<<<<<<<<<<<<<<\n\n")

except Exception as e:
    logger.exception(e)
    raise e

# Data Transformation
STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>>>>>>>>>> Stage: {STAGE_NAME} Started <<<<<<<<<<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>>>>>>> Stage: {STAGE_NAME} Completed <<<<<<<<<<<<<<<\n\n")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training Stage"

try:
    logger.info(f">>>>>>>>>>>>> Stage: {STAGE_NAME} Started <<<<<<<<<<<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>>>>>>>>> Stage: {STAGE_NAME} Completed <<<<<<<<<<<<<<<\n\n")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f">>>>>>>>>>>>> Stage: {STAGE_NAME} Started <<<<<<<<<<<<<<<")
    model_evaluator = ModelEvaluationPipeline()
    model_evaluator.main()
    logger.info(f">>>>>>>>>>>>> Stage: {STAGE_NAME} Completed <<<<<<<<<<<<<<<\n\n")

except Exception as e:
    logger.exception(e)
    raise e

