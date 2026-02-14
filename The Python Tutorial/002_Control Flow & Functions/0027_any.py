# any(iterable) -> bool
# - Returns True if at least one element of the iterable is truthy.
# - Returns False only if all elements are falsy (e.g., 0, '', None, False, etc.).
# - Works with any iterable (lists, tuples, sets, dicts, generators, etc.).
# - Uses short-circuit evaluation: stops as soon as a truthy value is found.
# - Commonly used in conditions to check if any condition or flag is true.
# - Returns False for an empty iterable.

# Basic examples:
print(any([False, False, True]))  # True
print(any([0, "", None]))  # False
print(any([]))  # False

# With strings
print(any("hello"))  # True (non-empty characters are truthy)
print(any(""))  # False (empty string is falsy)

# With tuples
print(any((0, 0, 5)))  # True
print(any((0, 0, 0)))  # False

# With sets
print(any({}))  # False (empty set)
print(any({0, "", None}))  # False
print(any({0, 1, 2}))  # True

# With generators (lazy evaluation)
print(any(x > 10 for x in [5, 8, 12]))  # True (12 > 10)
print(any(x < 0 for x in [1, 2, 3]))  # False

# With dictionary keys (only checks keys, not values)
d = {0: "zero", 1: "one"}
print(any(d))  # True (1 is truthy key)
d = {0: "zero", False: "no"}
print(any(d))  # False (all keys are falsy)

# Practical example - checking if any element satisfies a condition
numbers = [0, -2, 3, -1, 5]
print(any(n > 0 for n in numbers))  # True

# Using with custom functions
names = ["John", "", "Anna", ""]


def is_not_empty(name):
    return bool(name)


print(any(map(is_not_empty, names)))  # True
