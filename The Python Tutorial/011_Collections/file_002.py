# subtract(iterable_or_counter)
# Subtract counts from another iterable or counter, in place. Counts can go negative.
from collections import Counter

cnt1 = Counter(a=4, b=2, c=1)
cnt2 = Counter(a=1, b=3, d=2)

cnt1.subtract(cnt2)

# Display the result in a readable format
print("Result after subtraction:")
for key, value in cnt1.items():
    print(f"{key}: {value}")

"""
Result after subtraction:
a: 3
b: -1
c: 1
d: -2
"""

