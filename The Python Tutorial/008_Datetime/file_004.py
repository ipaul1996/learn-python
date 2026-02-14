# timedelta
# Represents a duration (difference between dates or times).
"""
Constructor:
timedelta(days=0, seconds=0, microseconds=0,
          milliseconds=0, minutes=0, hours=0, weeks=0)
"""
from datetime import date, timedelta

print(timedelta(days=1))  # 1 day, 0:00:00
print(timedelta(weeks=1))  # 7 days, 0:00:00
print(timedelta(hours=12))  # 12:00:00 # half day

today = date.today()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)

td = timedelta(days=1, seconds=3661, microseconds=500)
print(td.days)  # 1
print(td.seconds)  # 3661  (i.e. 1 h 1 min 1 s)
print(td.microseconds)  # 500
print(td.total_seconds())  # 90061.0005

print(type(td))  # <class 'datetime.timedelta'>


# We can do addition, subtraction, multiplication & division with timedelta objects
from datetime import timedelta

# Addition
td1 = timedelta(days=2, hours=3)
td2 = timedelta(hours=5, minutes=30)
result_add = td1 + td2
print("Addition:", result_add)  # 2 days, 8:30:00

# Subtraction
result_sub = td1 - td2
print("Subtraction:", result_sub)  # 1 day, 21:30:00

# Multiplication
result_mul = td1 * 2
print("Multiplication:", result_mul)  # 4 days, 6:00:00

# Division by integer
result_div = td1 / 2
print("Division:", result_div)  # 1 day, 1:30:00

# Division by timedelta (returns a float)
result_div_td = td1 / td2
print("Division (timedelta):", result_div_td)  # 9.272727272727273
