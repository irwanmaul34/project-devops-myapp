FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir \
    fastapi==0.137.2 \
    starlette==0.46.2 \
    uvicorn==0.34.2 \
    requests==2.32.3 \
    jinja2==3.1.6 \
    httpx==0.28.1

COPY main.py .
COPY templates/ templates/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
