from fastapi import FastAPI 
import pickle, 


app = FastAPI()

@app.get("/")
async def index():
    return {"Hello":"World"}

@app.post("/predict")
async def predict():
    with open()
    return ""