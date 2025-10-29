# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Imtiaz Mart - Product Service")

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

# In-memory database
products_db = [
    Product(id=1, name="Basmati Rice", price=250.0),
    Product(id=2, name="Pepsi 2L", price=180.0),
]

@app.get("/")
async def root():
    return {"service": "product-service", "status": "healthy"}

@app.get("/products", response_model=List[Product])
async def get_products():
    return products_db