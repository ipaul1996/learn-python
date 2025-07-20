from zoneinfo import ZoneInfo
from datetime import datetime, timezone, timedelta

# New York (with DST rules)
ny_dt = datetime.now(ZoneInfo("America/New_York"))

# Europe/Paris
paris_dt = datetime(2025, 3, 29, 2, 30, tzinfo=ZoneInfo("Europe/Paris"))



# Given an aware datetime:
dt_aware = datetime(2025, 7, 16, 12, tzinfo=timezone.utc)
ist = timezone(timedelta(hours=5, minutes=30), name="IST")

# Convert UTC → IST
ist_dt = dt_aware.astimezone(ist)

# Convert IST → New York
ny_dt = ist_dt.astimezone(ZoneInfo("America/New_York"))

print(dt_aware)  # 2025-07-16 12:00:00+00:00
print(ist_dt)  # 2025-07-16 17:30:00+05:30
print(ny_dt)  # 2025-07-16 08:00:00-04:00
