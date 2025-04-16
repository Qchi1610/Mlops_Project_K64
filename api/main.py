from fastapi import FastAPI, Query
from pydantic import BaseModel
import pandas as pd
import joblib
import wandb

# 🌟 Tạo app
app = FastAPI()

# 🌟 Kết nối W&B
run = wandb.init(project="Bank-Marketing", job_type="api")

# 🌟 Map tên model với tên artifact trong W&B
MODEL_ARTIFACTS = {
    "random_forest": "luquc-national-economics-university/Bank-Marketing/rf-model:latest",
    "logistic": "luquc-national-economics-university/Bank-Marketing/lr_model:latest"
}

# 🌟 Định nghĩa input
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
    duration: int
    campaign: int
    pdays: int
    previous: int
    poutcome: str
    emp_var_rate: float
    cons_price_idx: float
    cons_conf_idx: float
    euribor3m: float
    nr_employed: float

# 🌟 Route GET chào mừng
@app.get("/")
def home():
    return {"message": "Welcome to Mushroom Classifier API 👋"}

# 🌟 Route POST để dự đoán
@app.post("/predict")
def predict(input_data: BankInput, model_name: str = Query("random_forest")):
    # 1. Kiểm tra model_name
    if model_name not in MODEL_ARTIFACTS:
        return {"error": f"Model '{model_name}' not found. Choose from {list(MODEL_ARTIFACTS.keys())}"}
    
    # 2. Load model từ W&B artifact
    model_path = run.use_artifact(MODEL_ARTIFACTS[model_name]).file()
    model = joblib.load(model_path)

    # 3. Convert input về DataFrame
    df = pd.DataFrame([input_data.dict()])

    # 4. Dự đoán
    prediction = model.predict(df)[0]

    return {
        "model_used": model_name,
        "input": input_data.dict(),
        "prediction": "edible" if prediction == 0 else "poisonous"
    }
