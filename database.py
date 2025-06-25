from datetime import datetime, timedelta
from typing import List

classes = [
    {
        "id": 1,
        "name": "Yoga",
        "date_time": datetime.now() + timedelta(days=1),
        "instructor": "Alice",
        "available_slots": 5
    },
    {
        "id": 2,
        "name": "Zumba",
        "date_time": datetime.now() + timedelta(days=2),
        "instructor": "Bob",
        "available_slots": 3
    },
    {
        "id": 3,
        "name": "HIIT",
        "date_time": datetime.now() + timedelta(days=3),
        "instructor": "Charlie",
        "available_slots": 4
    },
]

bookings = []

def get_class_by_id(class_id):
    return next((c for c in classes if c["id"] == class_id), None)

def update_class_slots(class_id: int, delta: int):
    for c in classes:
        if c["id"] == class_id:
            c["available_slots"] += delta
            break

def add_booking(booking):
    bookings.append(booking)

def get_bookings_by_email(email):
    return [b for b in bookings if b["client_email"] == email]


def is_booking_exists(class_id,email):
    return any(b for b in bookings if b["class_id"] == class_id and b["client_email"] == email)