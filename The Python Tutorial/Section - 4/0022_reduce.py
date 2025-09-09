# reduce() Function
# reduce(function, iterable[, initializer]) -> value
# Applies function cumulatively to the items of iterable, returning a single result.
# Initializer (Optional): If provided, serves as the starting value and is placed before
# the items of the iterable.
# No Lazy Evaluation: Unlike map, reduce computes the final result immediately.
# Works with Any Iterable: Lists, tuples, etc., but must import from functools.

# If initializer is not given:
# - The first two elements of the iterable are passed to function, then the result and the next element, and so on.
# If initializer is given:
# - function(initializer, first_item) is computed first, then result with the next, etc.

from functools import reduce
import operator

nums = [1, 2, 3, 4]

# Without Initializer
product = reduce(operator.mul, nums)
# operator.mul(1, 2) => 2
# operator.mul(2, 3) => 6
# operator.mul(6, 4) => 24

# With Initializer
productV2 = reduce(operator.mul, nums, 1)
# operator.mul(1, 1) => 1
# operator.mul(1, 2) => 2
# operator.mul(2, 3) => 6
# operator.mul(6, 4) => 24


my_dict = {"a": 1, "b": 2, "c": 3}

total = reduce(lambda acc, item: acc + item[1], my_dict.items(), 0)
print(total)  # 6

maximum = reduce(max, nums)
print(maximum)  # 4

# Find the longest string in a list
words = ["cat", "elephant", "dog", "hippopotamus"]

longest_word = reduce(lambda a, b: a if len(a) > len(b) else b, words)
print(longest_word)  # hippopotamus
