from fastapi import FastAPI, Request, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
from utils import convert_timezone
from database import classes, bookings, get_class_by_id, update_class_slots, add_booking, get_bookings_by_email, is_booking_exists
from fastapi.responses import JSONResponse
import logging 
# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("booking_api")
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ValidateBookingRequest(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

class ValidateTimezone(BaseModel):
    timezone : str

class ValidateListBookings(BaseModel):
    email: EmailStr

@app.get("/classes")
def get_classes(timezone: Optional[str] = Query("Asia/Kolkata")):
    logger.info(f"Fetching classes in timezone: {timezone}")
    data = [
        {
            **c,
            "date_time": convert_timezone(c["date_time"], timezone)
        } for c in classes
    ]
    if data:
        logger.info("Listing classes")
        return JSONResponse({
            'status': True,
            'message': "success",
            'status_code': 200,
            'data': data
        }, status_code=200)
    else:
        return JSONResponse({
            'status': False,
            'message': "No classes found",
            'status_code': 400,
        }, status_code=400)



'''This api is used to book a class by providing customer email and class id'''
@app.post("/book")
def book_class(req: ValidateBookingRequest):
    logger.info(f"Book class API: {req.dict()}")
    fitness_class = get_class_by_id(req.class_id)
    if not fitness_class:
        logger.info(f"Class ID {req.class_id} not found")
        return JSONResponse({
        'status': False,
        'message': "Class not found",
        'status_code': 400,
    }, status_code=400)
 

    if fitness_class["available_slots"] <= 0:
        logger.info("No slots available")
        return JSONResponse({
        'status': False,
        'message': "No slots available",
        'status_code': 400,
    }, status_code=400)

    if is_booking_exists(req.class_id, req.client_email):
        logger.info("Duplicate booking attempt")
        return JSONResponse({
            'status': False,
            'message': "Booking already exists",
            'status_code': 400,
        }, status_code=400)

    update_class_slots(req.class_id, -1)
    add_booking(req.dict()) 
    logger.info(f"Booking successful for {req.client_email} in class {req.class_id}")
    status_code = 200
    return JSONResponse({
        'status': True,
        'message': "Booking successful",
        'status_code': status_code,
    }, status_code=status_code)

@app.get("/bookings")
def get_user_bookings(email: EmailStr):
    logger.info(f"List bookings API: {email}")
    data = get_bookings_by_email(email)
    if data:
        return JSONResponse({
            'status': True,
            'message': "success",
            'status_code': 200,
            'data': data
        }, status_code=200)

    else:
        return JSONResponse({
            'status': False,
            'message': "No Bookings available",
            'status_code': 400,
        }, status_code=400)
