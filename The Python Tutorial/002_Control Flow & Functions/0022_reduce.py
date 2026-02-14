"""
# reduce() Function
# reduce(function, iterable[, initializer]) -> Single Value
# Location: 'functools' module (Must be imported).

# It reduces an iterable to a single cumulative value by iteratively applying
# a function to an "accumulator" (running total) and the next item.

# The Logic Flow:

# Scenario A: No Initializer: reduce(func, [a, b, c])
#   - Step 1: accumulator = a (The first item is "consumed" to become the start value).
#   - Step 2: accumulator = func(accumulator, b)
#   - Step 3: accumulator = func(accumulator, c)
#
# Scenario B: With Initializer: reduce(func, [a, b, c], start)
#   - Step 1: accumulator = start (The external value is the start).
#   - Step 2: accumulator = func(accumulator, a)
#   - Step 3: accumulator = func(accumulator, b)
#
# Critical Rule for Initializer:
# If the output type (e.g., int) is different from the input item type (e.g., tuple),
# you MUST provide an initializer to set the correct starting type.
"""

from functools import reduce
import operator

nums = [1, 2, 3, 4]

# Basic Math (Product)

# Without Initializer:
# Logic: Starts with nums[0] (1).
# 1 * 2 = 2 -> 2 * 3 = 6 -> 6 * 4 = 24
product = reduce(operator.mul, nums)
print(product)  # 24

# With Initializer:
# Logic: Starts with Initializer (10).
# 10 * 1 = 10 -> 10 * 2 = 20 -> 20 * 3 = 60 -> 60 * 4 = 240
productV2 = reduce(operator.mul, nums, 10)
print(productV2)  # 240


# Type Transformation (The Dictionary Case)

my_dict = {"a": 1, "b": 2, "c": 3}

# We want to sum the VALUES (integers), but the ITEMS are TUPLES ('a', 1).
# Initializer '0' is required here to establish 'acc' as an integer.
# If omitted, 'acc' would start as the tuple ('a', 1), causing a TypeError.
total = reduce(lambda acc, item: acc + item[1], my_dict.items(), 0)
print(total)  # 6


# Comparative Reduction

# Finding the maximum number
# Logic: Compare 'acc' vs 'item'. Keep the larger one.
maximum = reduce(lambda a, b: a if a > b else b, nums)
print(maximum)  # 4

# Finding the longest string
words = ["cat", "elephant", "dog", "hippopotamus"]

# Logic: Compare current longest (a) vs new word (b). Keep the longer one.
longest_word = reduce(lambda a, b: a if len(a) > len(b) else b, words)
print(longest_word)  # hippopotamus
