# filter function
# filter(function, iterable) -> filter object
# - Applies the function to each element of the iterable.
# - Returns an iterator yielding only those elements for which the function returns True.
# - If function is None, returns elements that are true (non-false) by default.
# - The returned filter object computes values lazily as you iterate over it (e.g., with a for loop,
#   or by converting to a list, tuple, or set).
# - The original iterable is not modified.
# - Stops when the iterable is exhausted.
# - Works with any iterable (lists, tuples, sets, etc.).

numbers = [1, 2, 3, 4, 5, 6]


def is_even(x):
    return x % 2 == 0


print(filter(is_even, numbers))  # <filter object at 0x1010eb7f0>
print(list(filter(is_even, numbers)))  # [2, 4, 6]
print(tuple(filter(is_even, numbers)))  # (2, 4, 6)
print(set(filter(is_even, numbers)))  # {2, 4, 6}

# filter with lambda for concise code
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)  # Output: [1, 3, 5]

# filter with built-in functions
words = ["apple", "", "banana", "", "cherry"]
non_empty = list(filter(None, words))
print(non_empty)  # Output: ['apple', 'banana', 'cherry']

# filter over dictionary values
my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}


def is_odd(x):
    return x % 2 != 0


odd_values = list(filter(is_odd, my_dict.values()))
print(odd_values)  # Output: [1, 3]


# filter over dictionary items (e.g., keep items with even values)
def value_is_even(item):
    key, value = item
    return value % 2 == 0


even_items = dict(filter(value_is_even, my_dict.items()))
print(even_items)  #
