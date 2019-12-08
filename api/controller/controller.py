from fastapi import APIRouter

router=APIRouter()

@router.get("/")
async def root():
    return {'id':0000}




