FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./src /app/src

RUN pip install --no-cache-dir --upgrade -r /app/src/requirements.txt

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]