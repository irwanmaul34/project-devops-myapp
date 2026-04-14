from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

# folder templates wajib ada di /app/templates
templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )
