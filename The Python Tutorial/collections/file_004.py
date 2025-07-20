# defaultdict
# defaultdict is a subclass of dict from the collections module.
# It takes a factory function (default_factory) as its first argument.
# When you access a missing key, it automatically calls default_factory()
# to create and insert a default value, then returns it.
# This eliminates the need to check “if key in dict” before appending or incrementing values.

from collections import defaultdict

# Suppose you want to group names by their first letter
names = ["Alice", "Bob", "Arun", "Bella", "Chris"]

groups = defaultdict(list)  # default_factory is list

for name in names:
    key = name[0]  # first character
    groups[key].append(name)  # no KeyError—even if key is new

print(groups)
# defaultdict(<class 'list'>, {'A': ['Alice', 'Arun'], 'B': ['Bob', 'Bella'], 'C': ['Chris']})

print(dict(groups))  # {'A': ['Alice', 'Arun'], 'B': ['Bob', 'Bella'], 'C': ['Chris']}


# Using a regular dictionary
groupsV2 = {}  # plain dict

for name in names:
    key = name[0]  # first character
    if key not in groupsV2:
        groupsV2[key] = []
    groupsV2[key].append(name)

print(groupsV2)  # {'A': ['Alice', 'Arun'], 'B': ['Bob', 'Bella'], 'C': ['Chris']}
