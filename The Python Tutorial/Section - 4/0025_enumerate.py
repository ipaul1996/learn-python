# enumerate(iterable, start=0) -> enumerate object
# - Returns an iterator that yields pairs (index, item) for each item in the given iterable.
# - The index starts from the `start` value, defaulting to 0.
# - The result is an enumerate object, which supports lazy evaluation (values are produced on demand).
# - Useful for looping over items while keeping track of the index.
# - Works with any iterable: list, tuple, string, set, dict, generator, etc.

# Basic usage with list
items = ["a", "b", "c"]
for index, value in enumerate(items):
    print(index, value)
# Output:
# 0 a
# 1 b
# 2 c

# Using custom start index
for index, value in enumerate(items, start=1):
    print(index, value)
# Output:
# 1 a
# 2 b
# 3 c

# Converting enumerate object to list/tuple
enumerated = enumerate(["x", "y", "z"])
print(list(enumerated))  # [(0, 'x'), (1, 'y'), (2, 'z')]

# enumerate with strings
for i, ch in enumerate("hello"):
    print(i, ch)
# Output:
# 0 h
# 1 e
# 2 l
# 3 l
# 4 o

# enumerate with tuples
colors = ("red", "green", "blue")
for i, color in enumerate(colors):
    print(i, color)

# enumerate with set (note: sets are unordered)
unique_values = {"a", "b", "c"}
for i, val in enumerate(unique_values):
    print(i, val)

# enumerate with dictionary keys
my_dict = {"apple": 10, "banana": 20, "cherry": 30}
for i, key in enumerate(my_dict):
    print(i, key)

# enumerate with dictionary items
for i, (key, value) in enumerate(my_dict.items()):
    print(i, key, value)

# enumerate with generator
squares = (x * x for x in range(1, 4))
for i, val in enumerate(squares):
    print(i, val)
# Output:
# 0 1
# 1 4
# 2 9

# - enumerate is often used in loops where index tracking is needed
# - Cleaner alternative to manually incrementing index with a loop
# - Can be used with unpacking, list comprehensions, and in combination with zip/map/filter
