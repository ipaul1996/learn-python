# Variables are dynamically typed in Python, meaning we don't need to declare their type explicitly.
# Variable name can contain letters, numbers, and underscores, but cannot start with a number.

# Integer Assignment
x = 10  # An assignment statement (variable, operator, value)

# Float Assignment
y = 3.14

# String Assignment
name = "Alice"  # Immutable text

# Boolean Assignment
is_active = True

# List Assignment
fruits = ["apple", "banana", "cherry"]  # Ordered, mutable sequence

# Tuple Assignment
coordinates = (10.0, 20.0)  # Ordered, immutable sequence
coordinatesV2 = 10.0, 20.0  # Parentheses are optional when defining a tuple

# If the tuple has single element,
coordinatesV3 = (10.0,)
# If we do (10.0) it will be considered as a number, not a tuple

# Dictionary Assignment (key-value pairs)
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "isMarried": False,
    "family": ["Pichhi", "Mimi"],
}

# Set Assignment
unique_numbers = {1, 2, 3, 4, 5}  # Unordered, mutable collection of unique elements

# None Assignment
nothing = None  # a constant representing the absence of a value

# For variable naming we can not use reserved keywords:
"""
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
"""

# Multiple Assignments
a, b, c = 1, 2, 3  # Assigning multiple values to multiple variables
print(a, b, c)  # Output: 1 2 3


# ************************************************

# Unpacking sequences (like lists or tuples) into variables
nums = [4, 5, 6]

# Assign each element of the list to a separate variable
m, n, o = nums  # m=4, n=5, o=6

# If you try to unpack into fewer variables than elements, you'll get an error:
# k, p = nums      # ValueError: too many values to unpack (expected 2)

# ************************************************

# Extended unpacking: the * operator collects remaining elements into a list
k, p, *rest = nums  # k=4, p=5, rest=[6]
print(k, p, rest)  # Output: 4 5 [6]

# The * operator can also be used in the middle to collect all intermediate values
a, *b, c = [1, 2, 3, 4]
print(a, b, c)  # Output: 1 [2, 3] 4

# ************************************************

# Unpacking works with tuples as well
coords = (7, 8, 9)
x1, y1, z1 = coords  # x1=7, y1=8, z1=9

# Swapping values using tuple unpacking
x = 1
y = 2
x, y = y, x
print(x, y)  # Output: 2 1

r, p, *rest = (1, 2, 3, 7)
print(r, p, rest)  # Output: 1 2 [3, 7]

# ************************************************

# Set unpacking (note: sets are unordered, so variable assignment order is not guaranteed)
values = {10, 11, 12}
a1, b1, c1 = values  # The values will be assigned in arbitrary order, not predictable

# Extended unpacking with sets (order is still arbitrary)
numbers = {100, 200, 300, 400}
first, *rest = numbers
print("First:", first)
print("Rest:", rest)


# ************************************************

# Dictionary unpacking
d = {"x": 100, "y": 200, "z": 300}

# Unpacking only keys (default behavior)
k1, k2, k3 = d  # order is insertion order
print(k1, k2, k3)  # x y z

# To unpack values:
v1, v2, v3 = d.values()
# d.values() --> Returns a view object displaying a list of all the values in the dictionary.
print(v1, v2, v3)  # 100 200 300

# To unpack items (key-value pairs):
item1, item2, item3 = d.items()
print(item1, item2, item3)  # ('x', 100) ('y', 200) ('z', 300)
# d.items() --> Returns a view object displaying a list of the dictionary’s key-value pairs as tuples.
# dict_items([('x', 100), ('y', 200), ('z', 300)])


info = {"a": 10, "b": 20, "c": 30, "d": 40}

# Extended unpacking with dictionary keys
first_key, *middle_keys, last_key = info
print("First key:", first_key)  # a
print("Middle keys:", middle_keys)  # ['b', 'c']
print("Last key:", last_key)  # d

# Extended unpacking with dictionary values
first_val, *middle_vals, last_val = info.values()
print("First value:", first_val)  # 10
print("Middle values:", middle_vals)  # [20, 30]
print("Last value:", last_val)  # 40

# Extended unpacking with dictionary items
first_item, *middle_items, last_item = info.items()
print("First item:", first_item)  # ('a', 10)
print("Middle items:", middle_items)  # [('b', 20), ('c', 30)]
print("Last item:", last_item)  # ('d', 40)
