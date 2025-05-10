import requests

url = "http://127.0.0.1:8000/predict"
input_data = {
    "age": 45,
    "job": "housemaid",
    "marital": "married",
    "education": "basic.4y",
    "default": "no",
    "housing": "no",
    "loan": "no",
    "contact": "telephone",
    "month": "jun",
    "day_of_week": "thu",
    "duration": 245,
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

print("Request URL:", url)
print("Input data:")
for k, v in input_data.items():
    print(f"  {k}: {v}")

response = requests.post(url, params={"model_name": "LightGBM"}, json=input_data)
print("\nResponse:")
print("  Status code:", response.status_code)

try:
    print("  Response JSON:", response.json())
except Exception as e:
    print("  Error parsing response:", e)
    print("  Raw response text:", response.text)