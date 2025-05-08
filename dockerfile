# Dockerfile
FROM python:3.8-slim

# set workdir
WORKDIR /app

# copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy your code
COPY . .

# expose port (Render’s default 10000 or change as needed)
EXPOSE 10000

# start command
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
