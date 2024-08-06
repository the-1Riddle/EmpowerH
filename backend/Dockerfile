FROM python:3.11-buster

RUN mkdir app
WORKDIR /app

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY src/ .

# This would be used for production

# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Set the working directory
# WORKDIR /app

# Copy the requirements file
# COPY ./src/requirements.txt /app/requirements.txt

# Install dependencies
# RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy the application code
# COPY ./src /app/src

# Ensure the db directory exists
# RUN mkdir -p /app/db

# Command to run the application
# CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
