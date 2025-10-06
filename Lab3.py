'''
Convert meeting time across zones

Task: Given a UTC datetime for a meeting, return string times for "Asia/Kolkata", "America/New_York", "Europe/London".
'''
def meeting_slots(dt_utc: datetime) -> dict:
    zones = ["Asia/Kolkata", "America/New_York", "Europe/London"]
    return {z: dt_utc.astimezone(ZoneInfo(z)).strftime("%Y-%m-%d %H:%M %Z")
            for z in zones}

'''
Month calendar data structure

Task: Produce a list of ISO date strings for all actual days in Oct 2025.
'''
import calendar
from datetime import date

def days_in_month(year: int, month: int):
    _, last = calendar.monthrange(year, month)
    return [date(year, month, d).isoformat() for d in range(1, last+1)]

days_oct_2025 = days_in_month(2025, 10)

'''
Business hours duration

Task: Compute hours between two aware datetimes, counting only Mon-Fri 09:00-17:00 in the timezone of the start datetime.
'''
from datetime import time, timedelta, datetime

def business_hours(start: datetime, end: datetime) -> float:
    if start > end:
        start, end = end, start
    tz = start.tzinfo
    day = start.date()
    hours = 0.0
    while datetime.combine(day, time(0,0), tz) <= end:
        if 0 <= datetime.combine(day, time(0,0), tz).weekday() <= 4:
            open_dt = datetime.combine(day, time(9,0), tz)
            close_dt = datetime.combine(day, time(17,0), tz)
            a = max(open_dt, start)
            b = min(close_dt, end)
            if a < b:
                hours += (b - a).total_seconds() / 3600
        day = day + timedelta(days=1)
    return hours

'''
Human-friendly timestamp

Task: Write pretty_age(ts) that returns strings like “5m ago”, “2h ago”, “3d ago” for a POSIX timestamp ts (assume now in UTC).
'''
from datetime import datetime, timezone

def pretty_age(ts: float) -> str:
    now = datetime.now(timezone.utc)
    dt = datetime.fromtimestamp(ts, timezone.utc)
    delta = now - dt
    s = int(delta.total_seconds())
    if s < 60:   return f"{s}s ago"
    m = s // 60
    if m < 60:   return f"{m}m ago"
    h = m // 60
    if h < 24:   return f"{h}h ago"
    d = h // 24
    if d < 7:    return f"{d}d ago"
    w = d // 7
    return f"{w}w ago"

