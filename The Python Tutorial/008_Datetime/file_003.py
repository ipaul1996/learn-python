from datetime import date

d = date(2025, 7, 16)
print(d.isoformat())  # 2025-07-16 # YYYY-MM-DD

d1 = date.fromisoformat("2025-12-31")
print(d1)  # 2025-12-31

d2 = d1.replace(month=11, day=30)
# Returns a new date with new values for the specified fields.
print(d2)  # 2025-11-30

# Comparison
print(d1 > d2) # True