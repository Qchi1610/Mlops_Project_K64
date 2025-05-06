import os
from bank_mkt.constants import *
from dataclasses import dataclass
from datetime import datetime

TIMESTAMP: str = datetime.now().strftime("%m-%d-%Y-%H-%M-%S")

@dataclass
class TrainingPipelineConfig:
    pipeline_name: str = PIPELINE_NAME
    artifact_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP)
    timestamp: str = TIMESTAMP

