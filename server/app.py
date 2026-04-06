from fastapi import FastAPI

app = FastAPI()

state = {
    "focus_level": 50,
    "energy_level": 50,
    "blocked_apps": [],
    "notifications_sent": 0
}

@app.get("/")
def home():
    return {"message": "API Running"}

# ✅ IMPORTANT FIX
@app.api_route("/reset", methods=["GET", "POST"])
async def reset():
    global state
    state = {
        "focus_level": 50,
        "energy_level": 50,
        "blocked_apps": [],
        "notifications_sent": 0
    }
    return {"status": "reset successful", "state": state}