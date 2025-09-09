# sorted() Function
# Signature: sorted(iterable, *, key=None, reverse=False) -> list
# Returns a NEW sorted list from the items in an iterable.
# The original iterable is left unchanged.

## 1. Basic Sorting 🔢
# By default, sorted() sorts in ascending order.
data = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {data}")
print(f"Sorted:   {sorted(data)}")  # -> [1, 1, 2, 3, 4, 5, 6, 9]

# The `reverse=True` argument sorts in descending order.
print(f"Reversed: {sorted(data, reverse=True)}")  # -> [9, 6, 5, 4, 3, 2, 1, 1]
print(f"Original is unchanged: {data}")


## 2. The `key` Parameter: Sorting by a Custom Rule
# The `key` parameter specifies a function to be called on each element prior to making comparisons.
# It's like telling sorted() "how to see" each item.

# Example: Case-insensitive sort for strings
words = ["banana", "Apple", "almond", "Cherry"]
# Tell sorted() to "see" each word in its lowercase form for comparison.
print(sorted(words, key=str.lower))  # -> ['almond', 'Apple', 'banana', 'Cherry']

# Example: Sort strings by their length
print(sorted(words, key=len))  # -> ['Apple', 'banana', 'almond', 'Cherry']

# Example: Sort complex objects (like a list of tuples) by a specific index.
# Here, we use a lambda function to tell sorted() to look at the second element (index 1) of each tuple.
student_grades = [('Alice', 91), ('Bob', 85), ('Charlie', 95)]
print(sorted(student_grades, key=lambda student: student[1]))  # -> [('Bob', 85), ('Alice', 91), ('Charlie', 95)]


## 3. How `sorted()` Handles Different Types

# For tuples or lists, it sorts by the first element, then the second as a tie-breaker, and so on.
# This is called lexicographical sorting.
points = [[3, 1], [1, 5], [3, -2]]
print(sorted(points))  # -> [[1, 5], [3, -2], [3, 1]]

# For dictionaries, it sorts the keys by default.
d = {"b": 2, "a": 1, "c": 3}
print(sorted(d))  # -> ['a', 'b', 'c']

# To sort a dictionary by its values, use the key parameter.
print(sorted(d, key=d.get)) # -> ['a', 'b', 'c'] # type: ignore


## 4. Stable Sorting: Preserving Original Order ⚖️
# Python's sort is "stable". This means that if multiple items have the same key,
# their original relative order in the list is preserved.

# We will sort by the number (the second element).
# Note that 'apple' and 'kiwi' both have a value of 5.
inventory = [('apple', 5), ('banana', 2), ('kiwi', 5)]

# In the output, 'apple' still comes before 'kiwi' because it did in the original list.
print(sorted(inventory, key=lambda item: item[1])) # -> [('banana', 2), ('apple', 5), ('kiwi', 5)]