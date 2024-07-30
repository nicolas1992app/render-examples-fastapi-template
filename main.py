from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """
    Root endpoint returning a welcome message.
    """
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    """
    Endpoint to read an item by ID with an optional query parameter.
    
    Args:
    - item_id (int): The ID of the item.
    - q (str, optional): An optional query string.
    
    Returns:
    - dict: A dictionary containing the item ID and the query string.
    """
    return {"item_id": item_id, "q": q}