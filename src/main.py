from fastapi import FastAPI

app = FastAPI()

@app.get("/soma")
def soma(a: float, b: float):
    return {"resultado": a + b}

@app.get("/subtrai")
def subtrai(a: float, b: float):
    return {"resultado": a - b}

@app.get("/multiplica")
def multiplica(a: float, b: float):
    return {"resultado": a * b}

@app.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        return {"erro": "Divisão por zero não permitida"}
    return {"resultado": a / b}
