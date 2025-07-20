# Iterable

# In Python's typing module, Iterable is a generic type that represents
# any object capable of returning its members one at a time, i.e., Iterable[T]
# is a collection of items of type T that can be iterated over (e.g., list, tuple, set, dict, str, generator).
# Iterable guarantees you can use it in a for-loop, but does not guarantee indexing or length.

from typing import Iterable


def print_iterable(it: Iterable[int]) -> None:
    for item in it:
        print(item)


my_list: Iterable[int] = [1, 2, 3]
print_iterable(my_list)

# Things you can do with an Iterable:
# for item in it                # iterate items
# iter(it)                      # get iterator
# list(it), tuple(it), set(it)  # convert to list, tuple, set
# any(it), all(it)              # test truthiness
# sorted(it)                    # sorted items (returns a list)
# min(it), max(it)              # min/max item
# sum(it)                       # sum items
# zip(it1, it2, ...)            # zip multiple iterables
# filter(f, it), map(f, it)     # functional ops on items

# Note: Iterable does NOT guarantee random access (indexing), length, or mutability.
# For iterables that support indexing and length, use Sequence from
