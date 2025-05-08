FROM python:3.8-slim

# set workdir
WORKDIR /app

# install libgomp and build tools
RUN apt-get update && \
    apt-get install -y gcc g++ libgomp1 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy code
COPY . .

# expose port
EXPOSE 8000

# start
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
