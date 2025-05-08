import streamlit as st
import requests

API_URL = "https://mlops-project-k64.onrender.com"

st.title("Bank Marketing Prediction App")
st.markdown("Predict whether a customer will subscribe to a term deposit.")

# User inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30)
job = st.selectbox("Job", [
    "admin.", "blue-collar", "entrepreneur", "housemaid", "management",
    "retired", "self-employed", "services", "student", "technician",
    "unemployed", "unknown"
])
marital = st.selectbox("Marital Status", ["single", "married", "divorced", "unknown"])
education = st.selectbox("Education", [
    "basic.4y", "basic.6y", "basic.9y", "high.school",
    "illiterate", "professional.course", "university.degree", "unknown"
])
default = st.selectbox("Has Credit in Default?", ["yes", "no", "unknown"])
housing = st.selectbox("Has Housing Loan?", ["yes", "no", "unknown"])
loan = st.selectbox("Has Personal Loan?", ["yes", "no", "unknown"])
contact = st.selectbox("Contact Communication Type", ["cellular", "telephone"])
month = st.selectbox("Last Contact Month", [
    "jan", "feb", "mar", "apr", "may", "jun",
    "jul", "aug", "sep", "oct", "nov", "dec"
])
day_of_week = st.selectbox("Last Contact Day of the Week", ["mon", "tue", "wed", "thu", "fri"])
campaign = st.number_input("Number of Contacts in Current Campaign", min_value=1, value=1)
pdays = st.number_input("Days Since Last Contact (-1 or 999 if never)", value=999)
previous = st.number_input("Number of Contacts Before This Campaign", min_value=0, value=0)
poutcome = st.selectbox("Previous Campaign Outcome", ["failure", "nonexistent", "success"])
emp_var_rate = st.number_input("Employment Variation Rate", value=1.1)
cons_price_idx = st.number_input("Consumer Price Index", value=93.2)
cons_conf_idx = st.number_input("Consumer Confidence Index", value=-36.4)
euribor3m = st.number_input("Euribor 3-Month Rate", value=4.857)
nr_employed = st.number_input("Number of Employees", value=5191.0)
pdays_contacted_status = st.selectbox("Previously Contacted (1 = yes, 0 = no)", [0, 1])

# Submit button
if st.button("Predict"):
    input_data = {
        "age": age,
        "job": job,
        "marital": marital,
        "education": education,
        "default": default,
        "housing": housing,
        "loan": loan,
        "contact": contact,
        "month": month,
        "day_of_week": day_of_week,
        "campaign": campaign,
        "pdays": pdays,
        "previous": previous,
        "poutcome": poutcome,
        "emp_var_rate": emp_var_rate,
        "cons_price_idx": cons_price_idx,
        "cons_conf_idx": cons_conf_idx,
        "euribor3m": euribor3m,
        "nr_employed": nr_employed,
        "pdays_contacted_status": pdays_contacted_status,
    }

    try:
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"✅ Prediction: **{result['prediction'].upper()}**")
        else:
            st.error(f"❌ Error: {response.text}")
    except Exception as e:
        st.error(f"🚫 Could not connect to API: {e}")