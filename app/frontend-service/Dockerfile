FROM python:3.11-slim

WORKDIR /app
RUN pip install fastapi uvicorn requests jinja2

COPY main.py .
COPY templates templates

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
