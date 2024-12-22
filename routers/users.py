from fastapi import APIRouter, HTTPException, status
from db.models.users import User_Response, User
from db.services.users import insert_user, search_user_by_name

users_router = APIRouter()

@users_router.post("/users", response_model=User_Response, status_code=status.HTTP_201_CREATED)
async def create_new_user(user: User):
    if not search_user_by_name(user.name):
        insert_user(user)
        return search_user_by_name(user.name)
    else:
        raise HTTPException(status.HTTP_409_CONFLICT, detail="There is already a user with this name")

@users_router.get("/users/{name}", response_model=User_Response, status_code=status.HTTP_200_OK)
async def get_user(name: str):
    user = search_user_by_name(name)
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found")
    return user