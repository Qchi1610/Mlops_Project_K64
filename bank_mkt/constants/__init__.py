import os
from datetime import date

DATABASE_NAME = "Bank_mkt"

COLLECTION_NAME = "bank_mkt_data"

MONGODB_URL_KEY = "MONGODB_URL"

PIPELINE_NAME: str = "bank_mkt_pipeline"
ARTIFACT_DIR: str = "artifact"

MODEL_FILE_NAME = "model.pkl"

DATA_INGESTION_COLLECTION_NAME: str = "bank_mkt_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2
