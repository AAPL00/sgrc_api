from fastapi import APIRouter, HTTPException, status, Depends
from db.models.users import User_Response, User
from db.services.auth import auth_validaion, access_token
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

auth_router = APIRouter(prefix="/login")
auth = OAuth2PasswordBearer(tokenUrl="login")

@auth_router.post("/")
async def auth_login(form: OAuth2PasswordRequestForm = Depends()):
    user = auth_validaion(form.username, form.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_NOT_FOUND, detail="Invalid Auth")
    return access_token(user["name"])