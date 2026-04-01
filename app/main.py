# 1. Bring the FastAPI tool into our file
from fastapi import FastAPI

# 2. Initialize it (Turn the waiter on)
app = FastAPI()

# 3. Create the endpoint
# GET endpoint that returns {"status": "alive"}
@app.get("/")
def check_status():
    return {"status": "alive"}