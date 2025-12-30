from fastapi import FastAPI
import socket
import os

app = FastAPI()

@app.get("/")
def root():
    return {
        "service": "myapp",
        "message": "Hello from DevOps simple microservice 🚀",
        "hostname": socket.gethostname(),
        "env": os.getenv("ENVIRONMENT", "unknown")
    }

@app.get("/health")
def health():
    return Response(status_code=500)
