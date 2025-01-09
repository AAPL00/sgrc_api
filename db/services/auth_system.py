from db.client import client_db
from db.models.users import User_Response
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jwt import PyJWTError
import jwt
from datetime import datetime
from db.services.users import search_user_by_name

TOKEN_DURATION = 15
SECRET = "SALEM"
ALGORITHM = "HS256"

cript = CryptContext(schemes=["bcrypt"])
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

def login_verification(name: str, password: str):
    user = client_db.users.find_one({"name": name}, {"name": 1, "password": 1})
    return user["name"] if user and cript.verify(password, user["password"]) else None

def create_acces_token(name: str):
    access_token = {"sub": name,
                    "exp": datetime.utcnow() + timedelta(minutes=TOKEN_DURATION)}
    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "type": "bearer"}

def jwt_verification(token: str = Depends(oauth2)) -> User_Response:
    try:
        payload = jwt.decode(token, SECRET, algorithms=ALGORITHM)
    except PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token")
    
    
    sub = search_user_by_name(payload.get("sub", ""))
    exp = datetime.utcfromtimestamp(payload.get("exp"))

    if sub and exp and exp > datetime.utcnow():
        return sub
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token")