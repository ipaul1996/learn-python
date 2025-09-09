# map(function, iterable, *iterables) -> map object
# - Applies function to each element of the provided iterable(s), returning an iterator of results.
# - When additional iterables are supplied, function is called with one element from each iterable 
#   in parallel.
# - The returned map object computes values on-the-fly as you iterate over it; no results are
#   calculated until needed.(lazy evaluation)
# - The original iterables are not modified.
# - Stops when the shortest iterable is exhausted.
# - Works with any iterable (lists, tuples, sets, etc.).


characters = ['a', 'b', 'c', 'd']
print(map(str.upper, characters))         # <map object at 0x1010eb7f0>
print(list(map(str.upper, characters)))   # ['A', 'B', 'C', 'D']
print(tuple(map(str.upper, characters)))  # ('A', 'B', 'C', 'D')
print(set(map(str.upper, characters)))    # {'D', 'A', 'C', 'B'}

# map over dictionary values
my_dict = {'a': 1, 'b': 2, 'c': 3}
def square(x):
    return x ** 2

squared_values = list(map(square, my_dict.values()))
print(squared_values)  # Output: [1, 4, 9]

# map over dictionary keys
def to_upper(s):
    return s.upper()

my_dict = {'a': 1, 'b': 2, 'c': 3}
upper_keys = list(map(to_upper, my_dict.keys()))
print(upper_keys)  # Output: ['A', 'B', 'C']

# map over dictionary items
def double_item(item):
    key, value = item
    return (key, value * 2)

my_dict = {'a': 1, 'b': 2, 'c': 3}
doubled_dict = dict(map(double_item, my_dict.items()))
print(doubled_dict)  # Output: {'a': 2, 'b': 4, 'c': 6}

# - map() is often used with lambda functions for concise code.

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]


str_numbers = ['1', '2', '3']
int_numbers = list(map(int, str_numbers))
print(int_numbers)  # Output: [1, 2, 3]


a = [1, 2, 3]
b = [4, 5, 6]
summed = list(map(lambda x, y: x + y, a, b))
print(summed)  # Output: [5, 7, 9]


my_dict = {'a': 1, 'b': 2, 'c': 3}
# Get a list of squared values
squared_values = list(map(lambda v: v ** 2, my_dict.values()))
print(squared_values)  # Output: [1, 4, 9]


# - Function with Multiple Arguments: If you pass multiple iterables to map(), the function 
# you provide must accept the same number of arguments as there are iterables.
# Parallel Processing: map() will take one item from each iterable at the same position 
# and pass them as arguments to the function.
# Stops at Shortest Iterable: If the iterables are of different lengths, map() will stop 
# when the shortest iterable is exhausted.

# Two lists of numbers
a = [1, 2, 3]
b = [4, 5, 6, 7]

# Function that adds two numbers
def add(x, y):
    return x + y

# map applies 'add' to pairs from 'a' and 'b'
result = list(map(add, a, b))
print(result)  # Output: [5, 7, 9]


# - For side effects(such as printing to the console, modifying external variables, 
# or writing to a file), prefer using a for loop instead of map().

# - If we convert a map object to a list, tuple, or set, we exhaust the iterator. 
# We can’t reuse it.
m = map(str.upper, characters)
print(list(m))  # ['A', 'B', 'C', 'D']
print(list(m))  # [] (already exhausted)




