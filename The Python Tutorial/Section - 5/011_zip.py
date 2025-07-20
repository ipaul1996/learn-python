# zip(iterable1, iterable2, ...)
# The built-in zip() function takes two or more iterables (like lists, tuples,
# or strings) and returns an iterator of tuples, where the i-th tuple contains
# the i-th element from each of the input iterables.
# It pairs elements from each iterable by their position (index).
# The resulting iterator stops when the shortest input iterable is exhausted.
# You often convert the result to a list or tuple for display or further use.

a = [1, 2, 3]
b = ["x", "y", "z"]
zipped = zip(a, b)
print(list(zipped))  # [(1, 'x'), (2, 'y'), (3, 'z')]

# Unzipping
# You can also "unzip" a zipped object using the unpacking operator *
pairs = [(1, "x"), (2, "y"), (3, "z")]
a, b = zip(*pairs)
print(a)  # (1, 2, 3)
print(b)  # ('x', 'y', 'z')
