from fastapi.testclient import TestClient
from api.main import app  # đảm bảo đường dẫn đúng
import time
import os

client = TestClient(app)

# ✅ Test route GET /
def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert "Hello World" in r.text

# ✅ Test POST /predict với input hợp lệ - dự đoán có thể là yes hoặc no
def test_predict_valid_input():
    person = {
        "age": 35,
        "job": "technician",
        "marital": "married",
        "education": "tertiary",
        "default": "no",
        "housing": "yes",
        "loan": "no",
        "contact": "cellular",
        "month": "may",
        "day_of_week": "mon",
        "campaign": 1,
        "pdays": 999,
        "previous": 0,
        "poutcome": "nonexistent",
        "emp_var_rate": 1.1,
        "cons_price_idx": 93.994,
        "cons_conf_idx": -36.4,
        "euribor3m": 4.857,
        "nr_employed": 5191.0,
        "pdays_contacted_status": 0
    }

    r = client.post("/predict", json=person)
    assert r.status_code == 200
    assert r.json()["prediction"] in ["yes", "no"]

# ❌ Test POST /predict với key sai
def test_predict_invalid_key():
    person = {
        "age": 35,
        "job": "technician",
        "marital": "married",
        "educa": "tertiary",  # key sai (education -> educa)
        "default": "no",
        "housing": "yes",
        "loan": "no",
        "contact": "cellular",
        "month": "may",
        "day_of_week": "mon",
        "campaign": 1,
        "pdays": 999,
        "previous": 0,
        "poutcome": "nonexistent",
        "emp_var_rate": 1.1,
        "cons_price_idx": 93.994,
        "cons_conf_idx": -36.4,
        "euribor3m": 4.857,
        "nr_employed": 5191.0,
        "pdays_contacted_status": 0
    }

    r = client.post("/predict", json=person)
    assert r.status_code == 422  # vì sai key

# ❌ Test POST /predict với kiểu dữ liệu sai
def test_predict_wrong_type():
    person = {
        "age": "thirty",  # sai kiểu
        "job": "technician",
        "marital": "married",
        "education": "tertiary",
        "default": "no",
        "housing": "yes",
        "loan": "no",
        "contact": "cellular",
        "month": "may",
        "day_of_week": "mon",
        "campaign": 1,
        "pdays": 999,
        "previous": 0,
        "poutcome": "nonexistent",
        "emp_var_rate": 1.1,
        "cons_price_idx": 93.994,
        "cons_conf_idx": -36.4,
        "euribor3m": 4.857,
        "nr_employed": 5191.0,
        "pdays_contacted_status": 0
    }

    r = client.post("/predict", json=person)
    assert r.status_code == 422

# ⏱️ Test thời gian dự đoán
def test_prediction_time_under_3s():
    person = {
        "age": 35,
        "job": "technician",
        "marital": "married",
        "education": "tertiary",
        "default": "no",
        "housing": "yes",
        "loan": "no",
        "contact": "cellular",
        "month": "may",
        "day_of_week": "mon",
        "campaign": 1,
        "pdays": 999,
        "previous": 0,
        "poutcome": "nonexistent",
        "emp_var_rate": 1.1,
        "cons_price_idx": 93.994,
        "cons_conf_idx": -36.4,
        "euribor3m": 4.857,
        "nr_employed": 5191.0,
        "pdays_contacted_status": 0
    }

    start = time.time()
    r = client.post("/predict", json=person)
    elapsed = time.time() - start

    assert r.status_code == 200
    assert elapsed < 3
