from fastapi import APIRouter, HTTPException, status
from db.models.users import User_Response, User
from db.services.auth_system import search_user_by_name, insert_user

auth_router = APIRouter()

@auth_router.post("/new", response_model=User_Response, status_code=status.HTTP_201_CREATED)
async def create_new_user(user: User):
    if not search_user_by_name(user.name):
        insert_user(user)
        return search_user_by_name(user.name)
    else:
        raise HTTPException(status.HTTP_409_CONFLICT, detail="There is already a user with this name")
    
#@auth_router.post("/login", response_model=)