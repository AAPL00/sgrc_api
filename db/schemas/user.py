def user_schema(user) -> dict:
    return {"name": user["name"],
            "password": user["password"],
            "email": user["email"],
            "phone_number": user["phone_number"],
            "type": user["type"]}