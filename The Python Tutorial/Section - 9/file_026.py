# Comparison with built-ins

# Numbers (int, float)
# Support: ==, !=, <, <=, >, >=
print(3 == 3.0)  # True   (int and float compare numerically)
print(3 < 5)  # True
print(3 <= 3)  # True
print(10 > 7)  # True
print(5 >= 5.0)  # True
# All six operators work because int and float define __eq__, __lt__, etc.,
# and fall back to cross‐type implementations when needed.


# Strings
# Support: ==, !=, <, <=, >, >=
# Strings compare lexicographically (character by character), and
# implement the full set of ordering methods.
print("apple" == "Apple")  # False  (case sensitive)
print("apple" < "banana")  # True   (lexicographical order)
print("a" > "Z")  # True   (because lowercase > uppercase in Unicode code points)


# Sequences (list, tuple)
# Support: ==, !=, <, <=, >, >=
# Sequences are compared lexicographically: element by element, left to right.
# If all items are equal, the shorter sequence is considered less.
print([1, 2] == [1, 2])  # True
print([1, 2] < [1, 3])  # True   (compares 2 < 3)
print([1, 4] > [1, 3])  # True   (compares 4 > 3)
print((1, 2, 3) < (1, 2))  # False  (prefix matches, but left is longer)
print([1, 2] != [1, 2, 0])  # True   (different lengths)
print((1, 2) <= (1, 2, 0))  # True   (prefix matches, left is shorter)


# Mappings (dict)
# Support: only == and !=
# Dictionaries are unordered collections, so only equality and inequality comparisons are supported.
# Ordering comparisons (<, >, <=, >=) are not defined and will raise TypeError.
print({"a": 1, "b": 2} == {"b": 2, "a": 1})  # True   (order doesn’t matter)
print({"a": 1} != {"a": 2})  # True

try:
    print({} < {})
except TypeError as e:
    print(f"TypeError: {e}")  # '<' not supported between instances of 'dict' and 'dict'


# Sets (set, frozenset)
# Support: ==, !=, <=, <, >=, >
# Sets are unordered collections of unique elements.
# == and != test for equality of elements.
# <, <=, >, >= test for subset and superset relationships, not ordering.

print({1, 2, 3} == {3, 2, 1})  # True   (same elements, order doesn't matter)
print({1, 2} != {1, 2, 3})  # True   (different elements)
print({1, 2} < {1, 2, 3})  # True   (proper subset)
print({1, 2, 3} > {2})  # True   (proper superset)
print({1, 2} <= {1, 2, 3})  # True   (subset, may be equal)
print({1, 2, 3} >= {1, 2})  # True   (superset, may be equal)
print({1, 2, 3} < {1, 2, 3})  # False  (not a proper subset, equal)
print({1, 2, 3} <= {1, 2, 3})  # True   (subset, equal)
# Ordering comparisons (<, >, <=, >=) are based on subset/superset, not element order or value.
# Sets do not support ordering by value, so comparisons like {1, 2} < {3, 4} are False unless subset.


# Unrelated types
# Support: == and != only
# Ordering comparisons (<, >, <=, >=) between unrelated types raise TypeError.
# == and != always work, but objects of unrelated types are never considered equal.

print(3 == "3")  # False (int and str are unrelated types)
print([1, 2] != (1, 2))  # True (list and tuple are different types)

# Demonstrate TypeError for ordering comparisons between unrelated types
examples = [
    (3, "3", "<"),  # int < str
    ([1, 2], {"a": 1}, ">"),  # list > dict
    ((1, 2), [1, 2], "<="),  # tuple <= list
    ("apple", {1, 2, 3}, ">="),  # str >= set
]

for left, right, op in examples:
    try:
        # Dynamically perform the comparison based on the operator
        if op == "<":
            result = left < right
        elif op == ">":
            result = left > right
        elif op == "<=":
            result = left <= right
        elif op == ">=":
            result = left >= right
        print(f"{type(left).__name__} {op} {type(right).__name__}: {result}")
    except TypeError as e:
        print(
            f"TypeError: {type(left).__name__} {op} {type(right).__name__} is not supported ({e})"
        )
