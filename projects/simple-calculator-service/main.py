# main.py
from fastapi import FastAPI, Query

app = FastAPI(title="Simple Calculator Service")

@app.get("/")
async def root():
    return {"service": "simple-calculator", "status": "healthy"}

@app.get("/add")
async def add(a: float = Query(...), b: float = Query(...)):
    return {"operation": "add", "result": a + b}

@app.get("/multiply")
async def multiply(a: float = Query(...), b: float = Query(...)):
    return {"operation": "multiply", "result": a * b}

@app.get("/subtract")
async def subtract(a: float = Query(...), b: float = Query(...)):
    return {"operation": "subtract", "result": a - b}

@app.get("/divide")
async def divide(a: float = Query(...), b: float = Query(...)):
    if b == 0:
        return {"error": "Cannot divide by zero"}
    return {"operation": "divide", "result": a / b}
