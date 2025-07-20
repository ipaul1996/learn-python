# MutableMapping

# In Python's typing module, MutableMapping is a generic type that represents
# a mutable collection of key-value pairs, i.e., MutableMapping[K, V] is a mapping
# where each key of type K maps to a value of type V, and you can add, remove, or update items.
# The built-in dict implements MutableMapping.

from typing import MutableMapping


def update_mapping(m: MutableMapping[str, int], key: str, value: int) -> None:
    m[key] = value  # add or update
    m.popitem()  # remove last item


my_dict: MutableMapping[str, int] = {"a": 1, "b": 2}
update_mapping(my_dict, "c", 3)
print(my_dict)

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
# mapping[key] = value             # set or overwrite a key
# del mapping[key]                 # delete a key
# mapping.pop(key[, default])      # remove key and return its value
# mapping.popitem()                # remove and return an arbitrary (key, value)
# mapping.clear()                  # remove all items
# mapping.update(other)            # merge another mapping or iterable of pairs
# mapping.setdefault(key, default) # get or insert with default
# mapping.copy()                   # shallow copy (dict-specific)
