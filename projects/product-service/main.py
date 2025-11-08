# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import httpx

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


import httpx  # Add this import at the top
from fastapi import HTTPException

# Add this new endpoint inside your app
@app.get("/products/{product_id}/discounted-price")
async def get_discounted_price(product_id: int, discount_percent: float):
    # First, get the product details
    product = None
    for p in products_db:
        if p.id == product_id:
            product = p
            break
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Now call calculator-service to calculate the discounted price
    calculator_url = "http://calculator-service:8003/multiply"  # Docker service name
    params = {
        "a": product.price,
        "b": (100 - discount_percent) / 100  # e.g., 15% discount = multiply by 0.85
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(calculator_url, params=params)
    
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Calculator service error")
    
    result = response.json()
    discounted_price = result["result"]
    
    return {
        "original_price": product.price,
        "discount_percent": discount_percent,
        "discounted_price": discounted_price
    }

