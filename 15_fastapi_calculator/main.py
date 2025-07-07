from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()

@app.get("/add")
def get_addition(a: int, b: int):
	return {"result": a + b}

@app.get("/sub")
def get_subtraction(a: int, b: int):
	return {"result": a - b}

@app.get("/mult")
def get_multiply(a: int, b: int):
	return {"result": a * b}

@app.get("/div")
def get_divide(a: int, b: int):
	return {"result": a / b}

@app.get("/calc")
def get_operation(a: int, b: int, operation: str):
	if operation == 'add':
		result = a + b
	elif operation == 'sub':
		result = a - b
	elif operation == 'mult':
		result = a * b
	elif operation == 'div':
		result = a / b
	else:
		raise HTTPException(status_code=400, detail="Invalid operation")
	return {"result": result}