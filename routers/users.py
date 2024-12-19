from fastapi import APIRouter, HTTPException, status
from db.models.users import User, User_Response
from db.client import client_db
from db.services.user import search_user_by_name
from db.services.reservation import search_reservations_by_user

users_router = APIRouter(prefix="/users")

@users_router.post("/", response_model=User_Response, status_code=status.HTTP_201_CREATED)
async def save_user(user: User):
    user_dict = dict(user)
    if not search_user_by_name(user.name):
        client_db.users.insert_one(user_dict)
        return User_Response(**search_user_by_name(user.name))
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")

@users_router.get("/{name}")
async def get_other_user(name: str):
    return get_user(name)

@users_router.get("/{name}", response_model=tuple, status_code=status.HTTP_200_OK)
async def get_user_data(name: str):
    return (get_user(name), get_user_reservations(name))

def get_user(name: str):
    user = search_user_by_name(name)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return User_Response(**user)

def get_user_reservations(name: str):
    reservations = search_reservations_by_user(name)
    if not reservations:
        reservations = "There are no reservations under this user"
    return reservations

