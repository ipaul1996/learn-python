# AbstractSet

# In Python's typing module, AbstractSet is a generic type that represents
# a read-only (immutable) unordered collection of unique items, i.e., AbstractSet[T]
# is a collection of items of type T with no duplicates. The built-in set implements AbstractSet,
# but AbstractSet itself only guarantees read-only access (no mutation).

from typing import AbstractSet


def print_set(s: AbstractSet[int]) -> None:
    for item in s:
        print(item)


my_set: AbstractSet[int] = {1, 2, 3}
print_set(my_set)

# Things you can do with an AbstractSet:
# value in s                       # check membership
# len(s)                           # number of items
# for item in s                    # iterate items
# s.issubset(other), s <= other    # subset test
# s.issuperset(other), s >= other  # superset test
# s.isdisjoint(other)              # disjoint test
# s.union(other), s | other        # union
# s.intersection(other), s & other # intersection
# s.difference(other), s - other   # difference
# s.symmetric_difference(other), s ^ other # symmetric difference
# set(s), list(s)                  # convert to set or list
# min(s), max(s)                   # min/max item
# sorted(s)                        # sorted items (returns a list)
# filter(f, s), map(f, s)          # functional ops on items

# Note: AbstractSet does NOT support mutation (adding/removing items).
# For mutable sets, use Set
