from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/data")
def data():
    return {
        "service": "api-service",
        "hostname": socket.gethostname(),
        "value": 43
    }
