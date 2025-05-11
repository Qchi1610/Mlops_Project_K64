import sys
import os
import pytest
import pandas as pd
import wandb
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score, roc_auc_score
import joblib
current_dir = current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.insert(0, project_root)
from api.pipeline import NumericalTransformer, CategoricalTransformer, FeatureSelector
#print('import success')
#run = wandb.init(project="Bank-Marketing", job_type="test_with_pytest")
# ✅ Load artifacts once per session using fixture


@pytest.fixture(scope="session")
def artifact_paths():
    ''' Load artifacts from local directory '''
    artifact_dir = os.path.join(current_dir, 'artifacts')  # thư mục chứa các file đã lưu

    return {
        "train_data": os.path.join(artifact_dir, "train.csv-v5\\train.csv"),
        "test_data": os.path.join(artifact_dir, "test.csv-v5\\test.csv"),
        "encoder": os.path.join(artifact_dir, "target_encoder-v2\\target_encoder"),
        "model": os.path.join(artifact_dir, "model_export-v10\\model_export"),
    }

# ============================== TEST CASES ==============================

def test_load_train_data(artifact_paths):
    ''' Test loading train data from artifact '''
    df_train = pd.read_csv(artifact_paths["train_data"])
    assert df_train.shape == (31523, 21)

def test_load_test_data(artifact_paths):
    '''Test loading test data from artifact '''
    df_test = pd.read_csv(artifact_paths["test_data"])
    assert df_test.shape == (7881, 21)

def test_target_encoder(artifact_paths):
    ''' Test target encoder '''
    encoder = joblib.load(artifact_paths["encoder"])
    df_train = pd.read_csv(artifact_paths["train_data"])
    df_test = pd.read_csv(artifact_paths["test_data"])

    y_train = df_train["y"]
    y_test = df_test["y"]

    y_train_encoded = encoder.transform(y_train)
    y_test_encoded = encoder.transform(y_test)

    assert len(y_train_encoded) == len(y_train)
    assert len(y_test_encoded) == len(y_test)
    assert pd.Series(y_train_encoded).nunique() == 2
    assert pd.Series(y_test_encoded).nunique() == 2
