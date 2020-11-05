from pydantic import BaseModel
from datetime import datetime

class ChatMessageModel(BaseModel):
    id: str
    createdAt: datetime.datetime= datetime.now()
    speaker:str
    text:str