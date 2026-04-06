from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API Running"}

@app.api_route("/reset", methods=["GET", "POST"])
def reset():
    return {
        "status": "success",
        "message": "Reset working"
    }