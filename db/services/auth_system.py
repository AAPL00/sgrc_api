from db.client import client_db
from db.models.users import User, User_Response
from passlib.context import CryptContext
from datetime import datetime, timedelta

import jwt

TOKEN_DURATION = 15
SECRET = "SALEM"
ALGORITHM = "HS256"

cript = CryptContext(schemes=["bcrypt"])

def auth_user(name: str, password: str):
    user = client_db.users.find_one({"name": name}, {"name": 1, "password": 1})
    return user["name"] if user and cript.verify(password, user["password"]) else None

def create_acces_token(name: str):
    access_token = {"sub": name, "exp": datetime.utcnow() + timedelta(minutes=TOKEN_DURATION)}
    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "type": "bearer"}