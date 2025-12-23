from fastapi import FastAPI
import socket
import os

app = FastAPI()

@app.get("/")
def root():
    return {
        "service": "myapp",
        "message": "Hello from DevOps microservice 🚀",
        "hostname": socket.gethostname(),
        "env": os.getenv("ENVIRONMENT", "unknown")
    }

@app.get("/health")
def health():
    return {"status": "ok"}
