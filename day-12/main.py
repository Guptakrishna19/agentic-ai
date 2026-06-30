from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Pydantic model for request validation
class Item(BaseModel):
    name: str
    price: float
    quantity: int


# GET /hello
@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}


# GET /items/{item_id}
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}


# POST /items
@app.post("/items")
def create_item(item: Item):
    return {
        "message": "Item created successfully",
        "item": item
    }


# Sample data
items_db = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mouse", "price": 500},
    {"id": 3, "name": "Keyboard", "price": 1200},
    {"id": 4, "name": "Monitor", "price": 10000},
    {"id": 5, "name": "Headphones", "price": 2000},
]


@app.get("/items")
def get_items(skip: int = 0, limit: int = 10):
    return items_db[skip : skip + limit]