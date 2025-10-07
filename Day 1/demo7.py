from datetime import date, time, datetime, timezone, timedelta
from zoneinfo import ZoneInfo
'''
d = date(2025, 10, 6)
print(d)
t = time(14, 30,5, 12345)
print(t)
dt_naive = datetime(2025, 10, 6, 14, 30, 5, 12345)
print(dt_naive)
dt_utc = datetime(2025, 10, 6, 14, 30, 5, 12345, tzinfo=timezone.utc)
print(dt_utc)
dt_local = datetime(2025, 10, 6, 14, 30, 5, 12345, tzinfo=ZoneInfo("America/New_York"))
print(dt_local)

ts = dt_utc.timestamp()
print(ts)
dt_from_ts = datetime.fromtimestamp(ts, timezone.utc)
print(dt_from_ts)
'''
'''
#today / now
print(date.today())
print(datetime.now())
print(datetime.now(tz=timezone.utc))

#Build and impact
dt = datetime(2025, 10, 6, 9, 16, 0)
print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond)

# Arthimetic
one_week = timedelta(weeks=1)
print(dt + one_week)
print((dt + one_week) - dt)

#Date-only arithmetic
d1 = date(2025, 1, 1); d2 = date(2025, 10, 6)
print((d2 - d1).days)

from datetime import datetime, timezone
dt = datetime(2025, 10, 6, 16, 45, 9, tzinfo=timezone.utc)

print(dt.strftime("%Y-%m-%d"))           # 2025-10-06 (ISO-ish)
print(dt.strftime("%b %d, %Y"))          # Oct 06, 2025
print(dt.strftime("%I:%M %p %Z"))        # 04:45 PM UTC
print(dt.isoformat())                    # 2025-10-06T16:45:09+00:00

from datetime import datetime
s = "06-10-2025 09:15:00 +0530"
dt = datetime.strptime(s, "%d-%m-%Y %H:%M:%S %z")
# -> aware datetime with offset +05:30

#Converting between dates, times, timestamps

from datetime import datetime, timezone
from zoneinfo import ZoneInfo

native = datetime(2025, 10, 6, 9, 15)
US = ZoneInfo("America/New_York")
aware_local = native.replace(tzinfo=US)
'''

# Generating calenders

import calendar

print(calendar.month(2025, 10))
# HTML string:
html = calendar.HTMLCalendar(firstweekday=0).formatmonth(2025, 10)

# Iterate days of a month (0 means padding day outside the month)
for week in calendar.monthcalendar(2025, 10):
    print(week)

# Weekday helpers
print(calendar.weekday(2025, 10, 6))  # 0=Monday ... 6=Sunday
print(calendar.isleap(2028))          # True



