# Set

# In Python's typing module, Set is a generic type that represents
# an unordered collection of unique items, i.e., Set[T] is a collection
# of items of type T with no duplicates. The built-in set implements Set.
# Sets support mathematical set operations and mutation.

from typing import Set


def add_and_union(s: Set[int], value: int, other: Set[int]) -> Set[int]:
    s.add(value)  # add an item
    return s | other  # union with another set


my_set: Set[int] = {1, 2, 3}
result = add_and_union(my_set, 4, {3, 4, 5})
print(my_set)
print(result)

# Things you can do with a Set:
# value in s               # check membership
# len(s)                   # number of items
# for item in s            # iterate items
# s.add(value)             # add an item
# s.remove(value)          # remove an item (KeyError if not present)
# s.discard(value)         # remove if present, no error if not
# s.pop()                  # remove and return an arbitrary item
# s.clear()                # remove all items
# s.update(iterable)       # add multiple items
# s.union(other), s | other        # union
# s.intersection(other), s & other # intersection
# s.difference(other), s - other   # difference
# s.symmetric_difference(other), s ^ other # symmetric difference
# s.issubset(other), s <= other    # subset test
# s.issuperset(other), s >= other  # superset test
# s.isdisjoint(other)              # disjoint test
# set(s), list(s)                  # convert to set or list
# min(s), max(s)                   # min/max item
# sorted(s)                        # sorted items (returns a list)
# filter(f, s), map(f, s)          # functional ops on items

# Note: Set supports mutation (adding/removing items).
# For immutable sets, use FrozenSet
