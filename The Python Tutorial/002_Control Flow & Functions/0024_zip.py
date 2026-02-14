# zip(*iterables) -> zip object
# - Aggregates elements from two or more iterables, returning an iterator of tuples.
# - Each tuple contains one element from each iterable, grouped by their corresponding positions.
# - The returned zip object is lazy and only produces results as it is iterated over.
# - Stops when the shortest iterable is exhausted.
# - Works with any iterable (lists, tuples, sets, strings, etc.).


# Basic zip example
a = [1, 2, 3]
b = ["a", "b", "c"]
print(zip(a, b))  # <zip object at 0x1010eb7f0>
print(list(zip(a, b)))  # [(1, 'a'), (2, 'b'), (3, 'c')]
print(tuple(zip(a, b)))  # ((1, 'a'), (2, 'b'), (3, 'c'))

# Zipping three lists
a = [1, 2, 3]
b = ["a", "b", "c"]
c = [True, False, True]
print(list(zip(a, b, c)))  # [(1, 'a', True), (2, 'b', False), (3, 'c', True)]

# Stops at shortest iterable
a = [1, 2, 3, 4]
b = ["a", "b"]
print(list(zip(a, b)))  # [(1, 'a'), (2, 'b')]

# Zipping dictionary keys and values
my_dict = {"a": 1, "b": 2, "c": 3}
keys = my_dict.keys()
values = my_dict.values()
pairs = list(zip(keys, values))
print(pairs)  # [('a', 1), ('b', 2), ('c', 3)]

# zip is often used for parallel iteration
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Unzipping using * operator
zipped = [(1, "a"), (2, "b"), (3, "c")]
a, b = zip(*zipped)
print(a)  # (1, 2, 3)
print(b)  # ('a', 'b', 'c')

# Use with map for transformation
names = ["alice", "bob", "charlie"]
ages = [25, 30, 35]
capitalized = list(map(lambda t: (t[0].title(), t[1]), zip(names, ages)))
print(capitalized)  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# zip with different iterable types
letters = "abc"
numbers = (1, 2, 3)
print(list(zip(letters, numbers)))  # [('a', 1), ('b', 2), ('c', 3)]

# - If you convert a zip object to list, tuple, or set, you exhaust the iterator.
z = zip([1, 2], ["a", "b"])
print(list(z))  # [(1, 'a'), (2, 'b')]
print(list(z))  # [] (already exhausted)
