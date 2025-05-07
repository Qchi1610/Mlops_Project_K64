from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import pandas as pd
import joblib
import wandb
import os
import sys
from datetime import datetime
from pymongo import MongoClient
from api.pipeline import FeatureSelector, CategoricalTransformer, NumericalTransformer

# global variables
setattr(sys.modules["__main__"], "FeatureSelector", FeatureSelector)
setattr(sys.modules["__main__"], "CategoricalTransformer", CategoricalTransformer)
setattr(sys.modules["__main__"], "NumericalTransformer", NumericalTransformer)

# 🗄️ Cấu hình MongoDB
MONGODB_URI = os.getenv(
    "MONGODB_URI",
    "mongodb+srv://luquc11:luquc11@cluster0.ryesptx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)
DB_NAME = os.getenv("DB_NAME", "Bank_mkt")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "bank_mkt_input")

# Khởi kết nối MongoDB
tmp_client = MongoClient(MONGODB_URI)
db = tmp_client[DB_NAME]
collection = db[COLLECTION_NAME]

# initiate the wandb project
run = wandb.init(project="Bank-Marketing",job_type="api")

app = FastAPI()
ARTIFACT = "hangtn13-ssc-national-economics-university/Bank-Marketing/model_export:latest"

# Định nghĩa input
class BankInput(BaseModel):
    age: int
    job: str
    marital: str
    education: str
    default: str
    housing: str
    loan: str
    contact: str
    month: str
    day_of_week: str
    campaign: int
    pdays: int
    previous: int
    poutcome: str
    emp_var_rate: float
    cons_price_idx: float
    cons_conf_idx: float
    euribor3m: float
    nr_employed: float
    pdays_contacted_status: int

@app.get("/", response_class=HTMLResponse)
async def root():
    return "<h1>Bank Marketing Model API</h1>"

@app.post("/predict")
@app.post("/predict")
def predict(input_data: BankInput):
    try:
        model_export_path = run.use_artifact(ARTIFACT).file()
        pipe = joblib.load(model_export_path)
        df = pd.DataFrame([input_data.dict()])
        predict = pipe.predict(df)
        label = "no" if predict[0] <= 0.5 else "yes"

        # Log vào Mongo
        doc = { **input_data.dict(), "prediction": label, "timestamp": datetime.utcnow() }
        try:
            collection.insert_one(doc)
        except Exception as e:
            print("Mongo insert error:", e)

        return {"input": input_data.dict(), "prediction": label}
    
    except Exception as e:
        print("❌ Prediction Error:", e)
        raise HTTPException(status_code=500, detail=str(e))