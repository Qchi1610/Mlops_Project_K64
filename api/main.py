from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import pandas as pd
import joblib
import wandb
import sys
import os

# 🌟 Tạo app
app = FastAPI()

# 🌟 Map tên model với tên artifact trong W&B
MODEL_ARTIFACTS = {
    "random_forest": "Bank-Marketing/rf-model:latest",
    "logistic": "Bank-Marketing/lr_model:latest"
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
@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <p><span style="font-size:28px"><strong>Hello World</strong></span></p>"""\
    """<p><span style="font-size:20px">In this project, we will apply the skills """\
        """acquired in the Deploying a Scalable ML Pipeline in Production course to develop """\
        """a classification model on publicly available"""

# 🌟 Route POST để dự đoán
@app.post("/predict")
def predict(input_data: BankInput, model_name: str = Query("random_forest")):
    # Đăng nhập W&B nếu chưa đăng nhập
    if not wandb.run:
        wandb.login()

    # 1. Kiểm tra model_name
    if model_name not in MODEL_ARTIFACTS:
        return {"error": f"Model '{model_name}' not found. Choose from {list(MODEL_ARTIFACTS.keys())}"}
    
    # 2. Khởi tạo W&B run và load model từ W&B artifact
    run = wandb.init(project="Bank-Marketing", job_type="api", reinit=True)  # reinit=True để tránh khởi tạo lại nhiều lần
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
