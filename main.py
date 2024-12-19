from fastapi import FastAPI
from routers import users

app = FastAPI()

@app.get("/")
async def get():
    return "HOLA MUNDO"