# sorted() Function
# Signature: sorted(iterable, *, key=None, reverse=False) -> list
# Returns a NEW list containing all items from the iterable in ascending order.
# The original iterable is left UNCHANGED.

# Syntax Note: The asterisk (*) in the signature means that 'key' and 'reverse'
# are "Keyword-Only" arguments. You MUST write 'key=...' or 'reverse=...',
# you cannot just pass them as positional arguments.

## 1. Basic Sorting 🔢
# - Default behavior: Sorts numbers numerically and strings alphabetically.
# - Return Type: Always returns a List, even if you sort a tuple or dictionary.

data = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {data}")

# Standard ascending sort
print(f"Sorted:   {sorted(data)}")  # -> [1, 1, 2, 3, 4, 5, 6, 9]

# Descending sort (using reverse=True)
print(f"Reversed: {sorted(data, reverse=True)}")  # -> [9, 6, 5, 4, 3, 2, 1, 1]

# Verification that original data is untouched
print(f"Original is unchanged: {data}")


## 2. The `key` Parameter: Sorting by a Custom Rule
# The `key` argument expects a Function (callable).
# Logic: Python runs this function on every item *before* comparing them.
# It allows you to sort based on a "proxy" value rather than the item itself.

words = ["banana", "Apple", "almond", "Cherry"]

# Example A: Case-Insensitive Sort
# Logic: "See" 'Apple' as 'apple' and 'Cherry' as 'cherry' during comparison.
print(sorted(words, key=str.lower))
# -> ['almond', 'Apple', 'banana', 'Cherry']

# Example B: Sort by Length
# Logic: "See" 'Apple' as 5 and 'banana' as 6.
print(sorted(words, key=len))
# -> ['Apple', 'banana', 'almond', 'Cherry']

# Example C: Sort Complex Objects (Tuples/Lists) by specific index
# We want to sort students by their grade (Index 1).
student_grades = [("Alice", 91), ("Bob", 85), ("Charlie", 95)]

# "For each student, look at index 1"
print(sorted(student_grades, key=lambda s: s[1]))
# -> [('Bob', 85), ('Alice', 91), ('Charlie', 95)]


## 3. How `sorted()` Handles Different Types

# A. Lexicographical Sorting (Tuples/Lists)
# Logic: Compare item[0] first. If they are equal, compare item[1], etc.
points = [[3, 1], [1, 5], [3, -2]]
# [1, 5] comes first (1 < 3).
# [3, -2] comes before [3, 1] because -2 < 1.
print(sorted(points))  # -> [[1, 5], [3, -2], [3, 1]]

# B. Dictionaries
# Logic: Iterating over a dict only yields KEYS. So sorted(dict) returns sorted Keys.
d = {"b": 2, "a": 1, "c": 3}
print(sorted(d))  # -> ['a', 'b', 'c']

# To sort keys based on their VALUES:
# We tell sorted: "For every key 'k', look at 'd.get(k)' (the value)"
print(sorted(d, key=d.get))  # -> ['a', 'b', 'c'] # type: ignore


## 4. Stable Sorting: Preserving Original Order ⚖️
# Python's sort is "Stable".
# Definition: If two items have EQUAL keys, their original relative order
# from the source list is preserved in the output.

# Scenario: Sort by quantity (Index 1).
# 'apple' and 'kiwi' both have 5. 'apple' is before 'kiwi' in the input.
inventory = [("apple", 5), ("banana", 2), ("kiwi", 5)]

sorted_inventory = sorted(inventory, key=lambda item: item[1])

# Result: 'apple' stays before 'kiwi'.
print(sorted_inventory)
# -> [('banana', 2), ('apple', 5), ('kiwi', 5)]
