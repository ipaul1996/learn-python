# and, or, not

# Logical AND
a = True
b = False
print(a and b)  # Output: False
# Explanation: 'and' returns True only if both operands are True, otherwise False.

# Logical OR
print(a or b)  # Output: True
# Explanation: 'or' returns True if at least one operand is True, otherwise False.

# Logical NOT
print(not a)  # Output: False
# Explanation: 'not' inverts the boolean value (True becomes False, and vice versa).

# Combined usage
x = 5
y = 10
print(x > 0 and y < 20)  # Output: True
# Explanation: x > 0 is True and y < 20 is True, so the result is True.

print(x < 0 or y < 20)  # Output: True
# Explanation: x < 0 is False, but y < 20 is True, so 'or' returns True.

print(not (x == 5))  # Output: False
# Explanation: x == 5 is True, so not inverts the result i.e., False


# In Python, the logical operators and, or, and not can be used with any object.
# Every object in Python has an inherent boolean value. An object is considered "truthy"
# if it evaluates to True in a boolean context, and "falsy" if it evaluates to False.
# Falsy Values: False, None, 0, 0.0, 0j, "", [], (), empty dictionbary -> {}, empty set -> Set(),
# range(0), Decimal(0), Fraction(0, 1).
# Truthy Values: Everything else is considered truthy.
# An object you create will also be falsy if its special __bool__() method returns False or __len__()
# method returns 0. If neither is defined, the object is Truthy.

# or --> It returns the first truthy value it finds. If all values are falsy, it returns the last value.
# The or operator uses short-circuit evaluation, meaning it stops evaluating as soon as it encounters a truthy value.
result1 = 0 or "" or [1, 2]
print(result1)  # [1, 2]

result2 = None or 0 or []
print(result2)  # []

# and --> It returns the first falsy value it finds. If all values are truthy, it returns the last value.
# The and operator also uses short-circuit evaluation, meaning it stops evaluating as soon as it encounters a falsy value.
result4 = "hello" and [] and "world"
print(result4)  # []

result5 = "hello" and 42 and [1, 2]
print(result5)  # [1, 2]

# not x: This is the only operator that always returns a boolean. It returns False if x is truthy, and True if x is falsy.
result6 = not [1, 2, 3]
print(result6)  # False

result7 = not ""
print(result7)  # True
