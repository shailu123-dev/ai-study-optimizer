from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# -------- STATE --------
state = {
    "focus_level": 50,
    "energy_level": 50
}

# -------- REQUEST MODEL --------
class Action(BaseModel):
    action: str

# -------- RESET (VERY IMPORTANT) --------
@app.post("/reset")
def reset():
    global state
    state = {
        "focus_level": 50,
        "energy_level": 50
    }
    return {"status": "reset successful", "state": state}

# -------- STEP --------
@app.post("/step")
def step(action: Action):
    global state

    if action.action == "study":
        state["focus_level"] += 5
    elif action.action == "rest":
        state["energy_level"] += 5

    return {"state": state}

# -------- GET STATE --------
@app.get("/state")
def get_state():
    return state

# -------- ENTRY POINT --------
def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()