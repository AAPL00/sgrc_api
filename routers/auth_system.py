from fastapi import APIRouter, HTTPException, status, Depends
from db.services.auth_system import auth_user, create_acces_token
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

auth_router = APIRouter()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")
    
@auth_router.post("/login", status_code=status.HTTP_202_ACCEPTED)
async def login_user(form: OAuth2PasswordRequestForm = Depends()):
    name = auth_user(form.username, form.password)
    if not name:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Authentication failed")
    return create_acces_token(name)