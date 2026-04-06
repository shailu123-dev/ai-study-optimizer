from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API Running v2"}

# ✅ ADD THIS (THIS IS MISSING)
@app.post("/reset")
def reset():
    return {
        "status": "success",
        "message": "Reset working"
    }