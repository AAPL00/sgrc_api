from db.client import client_db
from db.schemas.user import user_schema

def search_user_by_name(name: str):
    user = client_db.users.find_one({"name": name})
    if not user:
        user = None
    else:
        user = user_schema(user)
    return user