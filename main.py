from fastapi import FastAPI
from routes.routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def read_root():
    return{"message": "Bem vindo a API d&d"}