from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

API_SERVICE_URL = "http://api-service/api/data"

@app.get("/")
def home(request: Request):
    status = "OK"
    data = None

    try:
        r = requests.get(API_SERVICE_URL, timeout=1)
        r.raise_for_status()
        data = r.json()
    except Exception:
        status = "API SERVICE DOWN"

    return templates.TemplateResponse(
        name="index.html",
        context={
            "request": request,
            "status": status,
            "data": data
        }
    )
