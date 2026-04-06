from fastapi import FastAPI

app = FastAPI()

# Dummy state
state = {
    "focus_level": 50,
    "energy_level": 50
}

# ✅ REQUIRED: RESET (POST)
@app.post("/reset")
async def reset():
    global state
    state = {
        "focus_level": 50,
        "energy_level": 50
    }
    return {"message": "Environment reset", "state": state}


# ✅ REQUIRED: STEP (POST)
@app.post("/step")
async def step(action: dict):
    global state
    
    # simple logic
    if action.get("action") == "study":
        state["focus_level"] += 5
    elif action.get("action") == "rest":
        state["energy_level"] += 5

    return {"state": state}


# ✅ REQUIRED: GET STATE (GET)
@app.get("/state")
async def get_state():
    return state


# ✅ REQUIRED ENTRY POINT
def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()