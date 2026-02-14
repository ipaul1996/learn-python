# The collections module in the Python standard library provides high-performance container datatypes.
# Some of the most commonly used classes include:
# Counter, defaultdict, OrderedDict, deque, namedtuple, ChainMap, and more.
# These classes can help you write cleaner, faster, and more readable code when working
# with collections of data.

# Counter is a subclass of dict specialized for counting hashable objects.
# Keys are the items you count; values are their counts (integers).
# Note: A hashable object is an object that has a fixed hash value during its lifetime.
# In Python, immutable types like strings, numbers, and tuples are hashable and
# can be used as keys in dictionaries. Mutable types like lists and dictionaries
# are not hashable and cannot be used as keys.

from collections import Counter

words = ["apple", "banana", "apple", "orange", "banana", "apple", "kiwi", "banana"]

# Crerate a Counter
fruits_counts = Counter(words)
print(fruits_counts)  # Counter({'apple': 3, 'banana': 3, 'orange': 1, 'kiwi': 1})

# Most Common Items
# Signature: most_common(self, n=None)
# Returns a list of the n most common elements and their counts, sorted from most to least common.
# n: (optional) The number of top items to return. If n is None, it returns all items sorted by count.
print(fruits_counts.most_common(2))  # [('apple', 3), ('banana', 3)]


# Update Counter with new elements
# Signature: update(iterable or mapping)
# Adds counts from the given iterable or mapping to the Counter.
# Existing counts are increased; new elements are added.
fruits_counts.update(["banana", "kiwi", "kiwi"])
print(fruits_counts)  # Counter({'banana': 4, 'apple': 3, 'kiwi': 3, 'orange': 1})


# elements()
# Returns an iterator over elements repeating each as many times as its count,
# in arbitrary order. Elements with a count of zero or less are ignored.
cnt = Counter(a=3, b=1, c=0)
list(cnt.elements())  # ['a', 'a', 'a', 'b']




# Converting Counter to dictionary
fruits_dict1 = dict(fruits_counts)
print(fruits_dict1)  # {'apple': 3, 'banana': 3, 'orange': 1, 'kiwi': 1}
