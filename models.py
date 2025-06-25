from pydantic import BaseModel, EmailStr
from datetime import datetime

class FitnessClass(BaseModel):
    id: int
    name: str
    date_time: datetime
    instructor: str
    available_slots: int

class Booking(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr