from pydantic import BaseModel
from datetime import datetime
from typing import Dict

class ChatMessageModel(BaseModel):
    id: str
    createdAt: Dict[str,datetime.datetime]= datetime.now()
    speaker:str
    text:str