# The time class represents a clock time without any date component.
from datetime import datetime, time

"""
Constructor signature:
time(hour: int = 0,
     minute: int = 0,
     second: int = 0,
     microsecond: int = 0,
     tzinfo: tzinfo | None = None,
     *, fold: int = 0) -> time

Parameters
– hour: 0–23
– minute, second: 0–59
– microsecond: 0–999999
– tzinfo: optional timezone (for “aware” times)
– fold: 0 or 1 (for ambiguous times around DST—rare)
"""
t1 = time(14, 30)  # 14:30:00
t2 = time(9, 15, 30, 500000)  # 09:15:30.500000
t3 = time(23, 59, 59)  # 23:59:59

# Core Attributes
print(t1.hour)  # 14
print(t1.minute)  # 30
print(t1.second)  # 0
print(t1.microsecond)  # 0
print(t1.tzinfo)  # None (unless set)
print(t1.fold)  # 0


t = time(7, 5, 9)
s = datetime.combine(datetime.today(), t).strftime("%I:%M:%S %p")
print(s)  # 07:05:09 AM
