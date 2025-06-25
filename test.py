import requests

BASE_URL = "http://127.0.0.1:8000"

def test_get_classes():
    timezone = "America/New_York"
    response = requests.get(f"{BASE_URL}/classes", params={"timezone": timezone})
    print("GET /classes Response:", response.json())

def test_book_class():
    payload = {
        "class_id": 1,
        "client_name": "John Doe",
        "client_email": "john@example.com"
    }
    response = requests.post(f"{BASE_URL}/book", json=payload)
    print("POST /book Response:", response.json())

def test_get_bookings():
    email = "john@example.com"
    response = requests.get(f"{BASE_URL}/bookings", params={"email": email})
    print("GET /bookings Response:", response.json())

if __name__ == "__main__":
    test_get_classes()
    test_book_class()
    test_get_bookings()
