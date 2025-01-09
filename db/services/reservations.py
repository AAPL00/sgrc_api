from db.client import client_db

def get_reservations_by_user_name(name: str):
    reservations_list = list(client_db.reservations.find({"user_name": name}))
    return reservations_list if reservations_list else "There are no reservations under this user"