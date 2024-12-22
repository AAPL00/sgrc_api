from fastapi import FastAPI
from routers.auth_system import auth_router
from routers.users import users_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(users_router)

@app.get("/")
async def get():
    return "HOLA MUNDO"