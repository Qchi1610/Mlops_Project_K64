import sys
import os
import pytest
import pandas as pd
import wandb

run = wandb.init(
    project="Bank-Marketing",
    job_type="data_checks"
)
@pytest.fixture(scope="session")
def data():
    local_path = run.use_artifact("Bank-Marketing/raw_data:latest").file()
    df = pd.read_csv(local_path)
    return df

def test_data_length(data):
    """
    We test that we have enough data to continue
    """
    assert len(data) > 1000

def test_number_of_columns(data):
    """
    We test that we have the correct number of columns
    """
    assert data.shape[1] == 21, f"Expected 21 columns, but got {data.shape[1]}"

def test_column_presence_and_type(data):
    required_columns = {
        "age": pd.api.types.is_int64_dtype,
        "job": pd.api.types.is_object_dtype,
        "marital": pd.api.types.is_object_dtype,
        "education": pd.api.types.is_object_dtype,
        "default": pd.api.types.is_object_dtype,
        "housing": pd.api.types.is_object_dtype,
        "loan": pd.api.types.is_object_dtype,
        "contact": pd.api.types.is_object_dtype,
        "month": pd.api.types.is_object_dtype,
        "day_of_week": pd.api.types.is_object_dtype,
        "duration": pd.api.types.is_int64_dtype,
        "campaign": pd.api.types.is_int64_dtype,
        "pdays": pd.api.types.is_int64_dtype,
        "previous": pd.api.types.is_int64_dtype,
        "poutcome": pd.api.types.is_object_dtype,
        "emp_var_rate": pd.api.types.is_float_dtype,
        "cons_price_idx": pd.api.types.is_float_dtype,
        "cons_conf_idx": pd.api.types.is_float_dtype,
        "euribor3m": pd.api.types.is_float_dtype,
        "nr_employed": pd.api.types.is_float_dtype,
        "y": pd.api.types.is_object_dtype
    }

    # Check column presence
    assert set(data.columns.values).issuperset(set(required_columns.keys()))

    for col_name, format_verification_funct in required_columns.items():
        assert format_verification_funct(data[col_name]), f"Column {col_name} failed test {format_verification_funct}"

def test_class_names(data):
    # Check that only the known classes are present for binary columns
    known_classes = ["yes", "no"]

    #assert data["default"].isin(known_classes).all(), f"Column default has unknown values: {data['default'].unique()}"
    #assert data["housing"].isin(known_classes).all(), f"Column housing has unknown values: {data['housing'].unique()}"
    #assert data["loan"].isin(known_classes).all(), f"Column loan has unknown values: {data['loan'].unique()}"
    assert data["y"].isin(known_classes).all(), f"Column y has unknown values: {data['y'].unique()}"

def test_categorical_values(data):
    # Check that categorical columns only contain allowed values
    job_categories = ['admin.','blue-collar','entrepreneur','housemaid','management','retired','self-employed','services','student','technician','unemployed','unknown']
    marital_status = ['unknown','married', 'divorced', 'single']
    education_levels = ['basic.4y','basic.6y','basic.9y','high.school','illiterate','professional.course','university.degree','unknown']
    contact_types = ['telephone', 'cellular']
    month_values = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    poutcome_values = ['nonexistent', 'failure', 'success']
    day_of_week_values = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

    assert data["job"].isin(job_categories).all(), f"Column job has unknown values: {data['job'].unique()}"
    assert data["marital"].isin(marital_status).all(), f"Column marital has unknown values: {data['marital'].unique()}"
    assert data["education"].isin(education_levels).all(), f"Column education has unknown values: {data['education'].unique()}"
    assert data["contact"].isin(contact_types).all(), f"Column contact has unknown values: {data['contact'].unique()}"
    assert data["month"].isin(month_values).all(),  f"Column month has unknown values: {data['month'].unique()}"
    assert data["poutcome"].isin(poutcome_values).all(), f"Column poutcome has unknown values: {data['poutcome'].unique()}"
    assert data["day_of_week"].isin(day_of_week_values).all(), f"Column day_of_week has unknown values: {data['day_of_week'].unique()}"

def test_column_ranges(data):
    # Add ranges for columns
    ranges = {
        "age": (0, 100),
        "duration": (0, 5000),  # Assuming the duration can be up to 5000 seconds
        "campaign": (0, 100),
        "pdays": (-1, 1000),  # -1 means client was not contacted previously
        "previous": (0, 100),
        "emp_var_rate": (-10, 10),  # Giả sử tỷ lệ biến động trong phạm vi này
        "cons_price_idx": (90, 110),  # Giả sử CPI dao động trong phạm vi này
        "cons_conf_idx": (-55, 55),  # Chỉ số niềm tin tiêu dùng thường trong phạm vi này
        "euribor3m": (0, 6),  # Lãi suất giữa các ngân hàng thường trong phạm vi này
        "nr_employed": (0, 10000),  # Số người có việc làm 
    }

    for col_name, (minimum, maximum) in ranges.items():
        assert data[col_name].dropna().between(minimum, maximum).all(), (
            f"Column {col_name} failed the test. Should be between {minimum} and {maximum}, "
            f"instead min={data[col_name].min()} and max={data[col_name].max()}"
        )
