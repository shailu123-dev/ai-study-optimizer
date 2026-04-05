from fastapi import FastAPI
from tasks.easy import run_easy_task
from tasks.medium import run_medium_task
from tasks.hard import run_hard_task

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Study Optimizer API Running"}

@app.get("/run")
def run_tasks():
    return {
        "easy": run_easy_task(),
        "medium": run_medium_task(),
        "hard": run_hard_task()
    }