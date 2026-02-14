# Mapping

# In Python's typing module, Mapping is a generic type that represents
# a read-only collection of key-value pairs, i.e., Mapping[K, V] is a collection
# where each key of type K maps to a value of type V. The built-in dict implements Mapping,
# but Mapping itself only guarantees read-only access (not mutation).

from typing import Mapping


def print_mapping(m: Mapping[str, int]) -> None:
    for key, value in m.items():
        print(f"{key}: {value}")


my_dict: Mapping[str, int] = {"a": 1, "b": 2}
print_mapping(my_dict)

# Things you can do with a Mapping:
# m[key]                   # get value by key
# key in m                 # check if key exists
# len(m)                   # number of items
# for key in m             # iterate keys
# m.keys()                 # get all keys
# m.values()               # get all values
# m.items()                # get all key-value pairs
# dict(m), list(m.items()) # convert to dict or list
# m.get(key[, default])    # get value with default
# m.setdefault(key, default) # get value or set default (dict only)
# min(m), max(m)           # min/max key
# sorted(m)                # sorted keys
# zip(m.keys(), m.values())# zip keys and values
# filter(f, m.items()), map(f, m.items()) # functional ops on items

# Note: Mapping does NOT support mutation (adding/removing items).
