from src.TextSummarizer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from src.TextSummarizer.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from src.TextSummarizer.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline
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

