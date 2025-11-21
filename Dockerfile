# Official python image
FROM python:3.12-slim

# Script in the add directory
WORKDIR /app

# Copied files (pyproject + source) and directories
COPY requirements.txt .
COPY ./app ./app

# For non-native library dependencies in Python (polars...)
RUN apt-get update && apt-get install -y build-essential

# Install dependencies
RUN pip install -r requirements.txt --no-cache-dir

# Network port for uvicorn
ENV PORT=8000

# Start command
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]