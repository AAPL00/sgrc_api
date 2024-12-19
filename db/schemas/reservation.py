def reservation_schema(reservation) -> dict:
    return {"id_space": reservation["id_space"],
            "id_user": reservation["id_user"],
            "start_date": reservation["start_date"],
            "end_date": reservation["end_date"],
            "state": reservation["state"]}