from fastapi import FastAPI
from routers import users

app = FastAPI()
app.include_router(users.users_router)

@app.get("/")
async def get():
    return "HOLA MUNDO"