# 📦 MLOps Project K64 – Bank Term Deposit Prediction

Welcome to the **MLOps Project K64** repository! This project implements a full MLOps pipeline to predict whether a bank client will subscribe to a term deposit, using the **Bank Marketing Dataset**.

---

## 📌 Project Overview

This project applies MLOps principles to the entire machine learning lifecycle, including:

- Data ingestion and preprocessing
- EDA (Exploratory Data Analysis)
- Model training, validation, and testing
- Model registry
- Streamlit interface for prediction
- MongoDB integration for test data storage

---

## 📊 Project Flow

![Flowchart](Flowchart.png)

---

## ⚙️ Technologies Used

- **Python 3.10**
- **scikit-learn**
- **pandas**, **numpy**, **matplotlib**, **seaborn**
- **MLflow** – for model tracking and registry
- **Streamlit** – for interactive user input and inference
- **MongoDB** – for storing new test input data
- **n8n** – optional future automation (e.g., retraining trigger)

---

## 🧰 Folder Structure
 Mlops_Project_K64/ │
├── artifacts/ # Stores processed data and models 
├── components/ # Reusable ML pipeline components 
├── config/ # YAML-based configuration files 
├── data/ # Raw and processed datasets 
├── logger/ # Logging configuration 
├── mlflow/ # MLflow experiments and registry 
├── notebook/ # EDA and testing notebooks 
├── pipelines/ # Training and testing pipelines 
├── prediction_service/ # Streamlit UI and MongoDB logic 
├── templates/ # YAML templates 
├── Flowchart.png # MLOps system diagram 
└── README.md ``` </code> </pre>
