from datetime import datetime, timezone, timedelta

"""
datetime(year: int,
         month: int,
         day: int,
         hour: int = 0,
         minute: int = 0,
         second: int = 0,
         microsecond: int = 0,
         tzinfo: tzinfo | None = None,
         *,
         fold: int = 0
        ) -> None
"""

# Naïve datetime (no tzinfo)
dt_naive = datetime(2025, 7, 16, 14, 30, 0, 123456)
print(dt_naive)  # 2025-07-16 14:30:00.123456
print(type(dt_naive))  # <class 'datetime.datetime'>

print(dt_naive.year)
print(dt_naive.month)
print(dt_naive.day)
print(dt_naive.hour)
print(dt_naive.minute)
print(dt_naive.second)
print(dt_naive.microsecond)

print(dt_naive.date())  # 2025-07-16
print(type(dt_naive.date()))  # <class 'datetime.date'>

print(dt_naive.time())  # 14:30:00.123456
print(type(dt_naive.time()))  # <class 'datetime.time'>

print(datetime.now()) # 2025-07-16 16:24:08.595765 (No Timezone Information)