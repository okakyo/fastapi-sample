from fastapi import FastAPI,Query

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/{id}")
async def getId(id: int):
    return {'id':id}

@app.get("/items/")
async def read_items(q: str = Query(None)):
    query_items = {"q": q}
    return query_items
