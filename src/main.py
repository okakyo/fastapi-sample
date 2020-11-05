from fastapi import FastAPI,Query
import controller.main as apiRouter 
from  controller.main import router as apiRouter

app = FastAPI()

@app.get("/")
def hello():
    return "Success"

app.include_router(
    apiRouter,
    prefix="/api",
    tags=["api"]
)

