from datetime import datetime
import pytz

def convert_timezone(dt: datetime, target_tz: str) -> str:
    ist = pytz.timezone("Asia/Kolkata")
    target = pytz.timezone(target_tz)
    dt_ist = ist.localize(dt)
    dt_converted = dt_ist.astimezone(target)

    # Format: "Wednesday, 25 June 2025 at 04:30 PM "
    return dt_converted.strftime("%A, %d %B %Y, %I:%M %p ")