# Arithmetic and Set‑Like Operations
# - Addition: c1 + c2 adds corresponding counts.
# - Subtraction: c1 - c2 subtracts, but discards zero or negative counts.
# - Intersection (&): takes the minimum of corresponding counts.
# - Union (|): takes the maximum of corresponding counts.

from collections import Counter

c1 = Counter(a=3, b=1, c=2)
c2 = Counter(a=1, b=2, d=4)

print(c1 + c2)  # Counter({'a': 4, 'd': 4, 'c': 2, 'b': 3})
print(c1 - c2)  # Counter({'a': 2, 'c': 2})      # drops b and d
print(c1 & c2)  # Counter({'a': 1, 'b': 1})      # min counts
print(c1 | c2)  # Counter({'d': 4, 'a': 3, 'b': 2, 'c': 2})  # max counts


# Create a shallow copy of c1
# We can modify it independently.
cnt = Counter(a=2, b=2)
cCopy = cnt.copy()
cCopy.update("a")
print(cnt)  # Counter({'a': 2, 'b': 2})
print(cCopy)  # Counter({'a': 3, 'b': 2})


# Clear all elements from the counter
cnt.clear()
print(cnt)  # Counter()


# Converting to Regular dict or List
# dict(cnt) gives you a plain dictionary.
# list(cnt) gives you just the distinct keys, in arbitrary order.
print(dict(cCopy))  # {'a': 3, 'b': 2}
print(list(cCopy))  # ['a', 'b']


