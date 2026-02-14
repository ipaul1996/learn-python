# OrderedDict
# OrderedDict is a subclass of dict that remembers insertion order of keys.
# Before Python 3.7, regular dicts did not guarantee order; OrderedDict was essential.
# From 3.7 onward, regular dict does preserve insertion order as an implementation detail,
# but OrderedDict still offers extra methods:
# - move_to_end(key, last=True): move an existing key to either end.
# - popitem(last=True): pop and return an item (LIFO if last=True, FIFO if last=False).

from collections import OrderedDict

od = OrderedDict()
od["apple"] = 1
od["banana"] = 2
od["cherry"] = 3

print(list(od.keys()))  # ['apple', 'banana', 'cherry'] # Insertion Order is Preserved

od.move_to_end("banana")  # move 'banana' to the end
print(list(od.keys()))  # ['apple', 'cherry', 'banana']

od.move_to_end("cherry", last=False)  # move 'cherry' to beginning
print(list(od.keys()))  # ['cherry', 'apple', 'banana']

last_item = od.popitem()  # pops last by default
print(last_item)  # ('banana', 2)

first_item = od.popitem(last=False)  # pops first
print(first_item)


# Equality considers order
od1 = OrderedDict([("a", 1), ("b", 2)])
od2 = OrderedDict([("b", 2), ("a", 1)])
print(od1 == od2)  # False # because order differs
