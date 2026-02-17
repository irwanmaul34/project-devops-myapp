from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/api/data")
def data():
    return {
        "service": "api-service",
        "hostname": socket.gethostname(),
        "value": 42
    }
