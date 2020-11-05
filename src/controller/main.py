from fastapi import APIRouter
import   logging 

router = APIRouter()

@router.get("/")
def hello():
    return {"message": "Hello World"}

@router.post("/predict")
def predict():
    try:
        logging.info("Done")
    except Exception as e :
        logging.error(e)


    return "Success"