from datetime import datetime, timezone, timedelta

dt = datetime.fromisoformat("2025-07-16T14:30:00+05:30")


# UTC timezone
print(timezone.utc)  # UTC
print(type(timezone.utc))  # <class 'datetime.timezone'>

# Define a timezone for UTC+5:30 (e.g., India Standard Time)
ist = timezone(timedelta(hours=5, minutes=30), name="IST")
print(ist)  # IST

# Define a timezone for UTC-8 (e.g., Pacific Standard Time)
pst = timezone(timedelta(hours=-8), name="PST")
print(pst)  # PST

# Signature: datetime.now(tz: tzinfo | None = None) -> datetime

utc_dt = datetime.now(timezone.utc)
print(utc_dt)  # 2025-07-16 10:36:08.056445+00:00

ist_dt = datetime.now(ist)
print(ist_dt)  # 2025-07-16 16:07:26.695573+05:30

pst_dt = datetime.now(pst)
print(pst_dt)  # 2025-07-16 02:38:53.291562-08:00

# We can do .year, .month, .day, .hour, .minute, .second, .microsecond on the datetime object(e.g., utc_dt)

print(utc_dt.date())  # 2025-07-16
print(utc_dt.time())  # 11:01:04.681789
print(utc_dt.weekday())  # 0=Mon … 6=Sun
print(utc_dt.isoweekday())  # 1=Mon … 7=Sun
print(utc_dt.isocalendar())  # datetime.IsoCalendarDate(year=2025, week=29, weekday=3)
year, week, weekday = utc_dt.isocalendar()
print(year, week, weekday)  # 2025 29 3

iso = utc_dt.isoformat()
print(iso)  # 2025-07-16T11:02:39.894990+00:00

s = utc_dt.strftime("%Y-%m-%d %H:%M:%S %Z")
print(s)  # 2025-07-16 11:15:34 UTC

ts = utc_dt.timestamp()  # float seconds since epoch
print(ts)  # 1752664566.799773
# Unix epoch or POSIX time is January 1, 1970, at 00:00:00 UTC

one_hour_later = utc_dt + timedelta(hours=1)
thirty_mins_ago = utc_dt - timedelta(minutes=30)

print(utc_dt.utcoffset())  # 0:00:00
print(utc_dt.tzname())  # UTC

print(ist_dt.utcoffset())  # 5:30:00
print(ist_dt.tzname())  # IST


print(utc_dt)  # 2025-07-16 11:33:49.734988+00:00

clean = utc_dt.replace(microsecond=0)  # Zero‑out microseconds
print(clean)  # 025-07-16 11:33:49+00:00

new_min = utc_dt.replace(minute=0, second=0, microsecond=0)  # Change to a fixed minute
print(new_min)  # 2025-07-16 11:00:00+00:00


