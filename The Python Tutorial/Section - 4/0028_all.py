# all(iterable) -> bool
# - Returns True if all elements of the iterable are truthy.
# - Returns False if any element is falsy.
# - Returns True for an empty iterable (vacuous truth).
# - The iterable can be a list, tuple, set, generator, dictionary, etc.
# - Stops evaluating as soon as a falsy value is found (short-circuiting).
# - Often used for input validation, all-pass filters, or strict checks.


# All elements are True
values = [True, 1, "non-empty", [1]]
print(all(values))  # True

# At least one element is False
values = [True, 0, "text"]
print(all(values))  # False

# Empty iterable
print(all([]))  # Output: True (vacuous truth)

# Using all() with list comprehension
numbers = [2, 4, 6, 8]
print(all(n % 2 == 0 for n in numbers))  # True

numbers = [1, 2, 4, 6]
print(all(n % 2 == 0 for n in numbers))  # False

# Check if all dictionary values are non-empty
my_dict = {"a": 1, "b": 2, "c": []}
print(all(my_dict.values()))  # False

my_dict = {"a": 1, "b": 2, "c": 3}
print(all(my_dict.values()))  # True

# all() on sets
s = {1, 2, 3}
print(all(s))  # True

s = {0, 1, 2}
print(all(s))  # False

# With generator (lazy evaluation)
numbers = range(1, 1000000)
print(all(n > 0 for n in numbers))  # True (efficient)
