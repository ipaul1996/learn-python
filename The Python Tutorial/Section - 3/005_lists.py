# list
# A list is a collection of items in a particular order.
# Lists are mutable, meaning you can change their content.
squares = [1, 4, 9, 16, 25]
empty_list = []  # An empty list
print(squares)
print(empty_list)

# Lists can contain different types of items
mixed_list = [1, "two", 3.0, True]
print(mixed_list)

# Lists can be nested, meaning a list can contain other lists
nested_list = [1, [2, 3], [4, 5, 6]]
print(nested_list)

# Accessing list items
print(squares[0])  # 1 # First item
print(squares[-1])  # 25 # Last item
print(squares[len(squares) - 1])  # 25 Last item using length
print(squares[-len(squares)])  # 1 # First item using negative indexing

# Slicing lists
# Slicing returns a new list containing the specified range of items
print(squares[1:3])  # Items from index 1 to 2 (4, 9)
print(squares[:3])  # First three items [0,3) [1, 4, 9]
print(squares[3:])  # Items from index 3 to the end [3, len(squares)) (16, 25)


# Modifying lists
squares[0] = 0  # Change the first item to 0
print(squares)  # [0, 4, 9, 16, 25]

# list concatenation
squares = squares + [36, 49, 64]  # Concatenate another list
print(squares)  # [0, 4, 9, 16, 25, 36, 49, 64]

# list repetition
squares = squares * 2  # Repeat the list
print(squares)  # [0, 4, 9, 16, 25, 36, 49, 64, 0, 4, 9, 16, 25, 36, 49, 64]

# List length
print(len(squares))  # Length of the list (16)

# Adding items to a list
squares.append(81)  # Add an item to the end of the list
print(squares)  # [0, 4, 9, 16, 25, 36, 49, 64, 0, 4, 9, 16, 25, 36, 49, 64, 81]

# Assigning a list to another variable does NOT create a copy.
# Both variables refer to the same list object in memory.
another_list = squares
print(id(squares) == id(another_list))  # True: both refer to the same object
print(
    id(squares), id(another_list)
)  # 4309678720 4309678720 # identical memory addresses
print(another_list is squares)  # True: both refer to the same object
# The id() function in Python returns the “identity” of an object(the memory address where
# the object is stored). This identity is unique and constant for the object during its lifetime.

# Modifying the list through one variable affects the other,
# since they are just two names for the same list.
another_list[0] = 100  # Change the first item via another_list

# The change is visible through both variables.
print(squares)  # [100, 4, 9, 16, 25, 36, 49, 64, 0, 4, 9, 16, 25, 36, 49, 64, 81]


# We can assign to slices to replace, insert, or remove multiple items at once.
# This can change the size of the list or even clear it entirely.

# syntax: list[start:end:step] = iterable
# - start: Index of the list to begin replacing (inclusive). Defaults to 0, if omitted.
# - end: Index of the list to stop replacing (exclusive). Defaults to len(list), if omitted.
# - step: How many indices to skip between replacements. Defaults to 1.
# - iterable: The sequence of new values to assign to the selected slice.
#
# If step is 1 (or omitted):
#   - If start < end, replaces elements from start (included) to end (excluded) with elements from the iterable.
#   - If start == end or start > end, inserts elements from the iterable at the start index.
#
# If step is not 1:
#   - The slice selects non-contiguous elements (for example, every second or third element) in the list for replacement.
#   - The number of items in the iterable must exactly match the number of elements selected by the slice in the list.
#   - Each element in the iterable replaces the corresponding element at the positions of the list specified by the slice.
#   - Elements at positions start, start+step, start+2*step, ... are replaced by elements from the iterable.
fruits = ["apple", "banana", "cherry"]
fruits[1:2] = ["blueberry", "blackberry"]  # Replace "banana" with two new fruits
print(fruits)  # ["apple", "blueberry", "blackberry", "cherry"]

fruits[0:1] = []  # Remove the first fruit
print(fruits)  # ["blueberry", "blackberry", "cherry"]

fruits[:] = []  # Clear the entire list
print(fruits)  # []

# Replace 3 middle elements with [10, 20, 30]
a = [1, 2, 3, 4, 5]
a[1 : len(a) - 1] = [10, 20, 30]
print(a)  # [1, 10, 20, 30, 5]


# Insert ['x', 'y'] b/w 'b' and 'c'
b = ["a", "b", "c", "d"]
b[2:2] = ["x", "y"]
print(b)  # ['a', 'b', 'x', 'y', 'c', 'd']

# Remove the elements at indices 2, 3, and 4
c = [0, 1, 2, 3, 4, 5, 6]
c[2:5] = []
print(c)  # [0, 1, 5, 6]

# Replace every second element with 0
d = [1, 2, 3, 4, 5, 6]
d[::2] = [0] * (len(d) // 2)
print(d)  # [0, 2, 0, 4, 0, 6]

# Replace every third element with -1
m = [0, 1, 2, 3, 4, 5, 6, 7, 8]
m[::3] = [-1] * (len(m) // 3)
print(m)  # [-1, 1, 2, -1, 4, 5, -1, 7, 8]

# Replace every second element between indices x and y (not including y) with -2
x = 1
y = 5
p = [0, 1, 2, 3, 4, 5, 6, 7, 8]
p[x:y:2] = [-2] * ((y - x) // 2)
print(p)  # [0, -2, 2, -2, 4, 5, 6, 7, 8]
