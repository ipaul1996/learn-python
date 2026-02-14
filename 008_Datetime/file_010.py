from datetime import datetime, time, timedelta, timezone

t = time(14, 30, 15, 123456)
print(t.isoformat())  # 14:30:15.123456

tz = timezone(timedelta(hours=2))
t_aware = time(8, 0, tzinfo=tz)
print(t_aware.isoformat())  # 08:00:00+02:00


t1 = time(9, 0)
t2 = time(17, 0)
print(t1 < t2)  # True
print(t1 == time(9, 0))  # True
# Note: Comparing aware vs. naïve raises TypeError.
