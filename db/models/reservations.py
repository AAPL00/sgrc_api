from pydantic import BaseModel
from datetime import datetime

class Reservations(BaseModel):
    user_name: str
    space_name: str
    start_time: datetime
    end_time: datetime
    state: int #0-pendiente, 1-confirmada