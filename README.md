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

## 📚 Dataset Information

This project uses the **Bank Marketing Dataset** with social and economic features, made publicly available for research purposes.

> **Citation Request**  
> If you use this dataset, please cite:  
> **[Moro et al., 2014]** S. Moro, P. Cortez, and P. Rita.  
> *A Data-Driven Approach to Predict the Success of Bank Telemarketing*.  
> Decision Support Systems. [DOI: 10.1016/j.dss.2014.03.001](http://dx.doi.org/10.1016/j.dss.2014.03.001)  
> - [PDF](http://dx.doi.org/10.1016/j.dss.2014.03.001)  
> - [BibTeX](http://www3.dsi.uminho.pt/pcortez/bib/2014-dss.txt)

### 🔍 Source

- Created by: Sérgio Moro, Paulo Cortez, and Paulo Rita (2014)  
- Original UCI Repository: [Bank Marketing Dataset](http://archive.ics.uci.edu/ml/datasets/Bank+Marketing)

### 📌 Dataset Variants

- `bank-additional-full.csv`: Full dataset (41,188 instances)
- `bank-additional.csv`: 10% subset (4,119 instances), suitable for computationally intensive models

### 🧠 Prediction Task

- **Goal**: Predict if a customer will subscribe to a term deposit (target: `y`, values: `yes` or `no`)

---

### 📈 Features Overview

| Feature Group | Attributes |
|---------------|------------|
| **Client Info** | `age`, `job`, `marital`, `education`, `default`, `housing`, `loan` |
| **Last Contact** | `contact`, `month`, `day_of_week`, `duration`* |
| **Campaign Data** | `campaign`, `pdays`, `previous`, `poutcome` |
| **Social/Economic** | `emp.var.rate`, `cons.price.idx`, `cons.conf.idx`, `euribor3m`, `nr.employed` |
| **Target** | `y` (binary: `yes` / `no`) |

> ⚠️ **Note on `duration`**: This feature strongly affects the output but is only known after the call. It should be excluded in realistic predictive models and used only for benchmarking.

---

### ⚠️ Missing Values

Some categorical features contain missing values labeled as `"unknown"`. You may choose to:
- Treat `"unknown"` as a separate category
- Remove or impute these values based on context

---

For full attribute definitions, see the paper:  
**[Moro et al., 2014]** *A Data-Driven Approach to Predict the Success of Bank Telemarketing*


