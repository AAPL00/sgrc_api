from pydantic import BaseModel
from datetime import datetime

class Reservation(BaseModel):
    id_space: str
    id_user: str
    start_date: datetime
    end_date: datetime 
    state: int #0-waiting, 1-confirmed, -1-canceled