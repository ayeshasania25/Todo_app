from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

todos = []

@app.get("/", response_class=HTMLResponse)
def read_todos(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "todos": todos}
    )

@app.post("/add")
def add_todo(title: str = Form(...)):
    todos.append(title)
    return RedirectResponse(url="/", status_code=303)

@app.post("/delete/{todo_id}")
def delete_todo(todo_id: int):
    if 0 <= todo_id < len(todos):
        todos.pop(todo_id)
    return RedirectResponse(url="/", status_code=303)
