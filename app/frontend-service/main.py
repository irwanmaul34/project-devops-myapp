from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

API_SERVICE_URL = "http://api-service/data"

@app.get("/")
def home(request: Request):
    status = "OK"
    data = {}

    try:
        r = requests.get(API_SERVICE_URL, timeout=1)
        data = r.json()
    except Exception:
        status = "API SERVICE DOWN"

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "status": status,
            "data": data
        }
    )
