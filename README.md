# Mlops_Project_K64

## Environment

Initial env
```bash
conda create -n bankmkt python=3.8 -y
conda activate bankmkt
pip install -r requirements.txt
``` 

Chạy lệnh sau để conda tự tạo env bankmkt
```bash
conda env create -f environment.yml
```
Lệnh chạy api
```bash
uvicorn api.main:app --reload
```

lệnh test_main
```bash
pytest api/test_main.py
```
lệnh chạy query_live_api
```bash
python api/query_live_api.py
```
lệnh chạy streamlit
```bash
streamlit run api/app.py
```

<kbd> <br> [Bank Marketing App][https://mlopsprojectk64.streamlit.app] <br> </kbd>
