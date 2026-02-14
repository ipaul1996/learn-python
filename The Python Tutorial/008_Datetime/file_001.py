# Fundamentals of Date & Time: https://mammoth-clementine-fbb.notion.site/Fundamentals-of-Date-Time-128f4d9da8c280af833bea76e96bc06e

# The built‑in datetime module provides classes for manipulating dates and times in both simple and complex ways.
# import datetime
# from datetime import date, time, datetime, timedelta, timezone

# Key Classes & Constructors:
# date -> Represents a calendar date (year, month, day). Constructor -> date(year: int, month: int, day: int)
# time -> Represents a time of day (hour, minute, etc.). Constructor ->	time(hour: int=0, minute: int=0, second: int=0, microsecond: int=0, tzinfo: tzinfo=None)
# datetime -> Combines date and time. Constructor -> datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
# timedelta -> Difference between two dates/times. Constructor -> timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
# timezone -> Fixed offset from UTC. Constructor -> timezone(offset: timedelta, name: Optional[str]=None)

from datetime import date

today = date.today()
print(today)  # 2025-07-16 (Local Date)

print(today.year, today.month, today.day)  # 2025 7 16
print(today.weekday())  # e.g. 2  (0=Monday → Wednesday)
print(today.isoweekday())  # e.g. 3  (1=Monday → Wednesday)

print(type(today))  # <class 'datetime.date'>
