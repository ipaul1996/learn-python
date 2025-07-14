# and, or, not

# Logical AND
a = True
b = False
print(a and b)  # Output: False
# Explanation: 'and' returns True only if both operands are True.

# Logical OR
print(a or b)   # Output: True
# Explanation: 'or' returns True if at least one operand is True.

# Logical NOT
print(not a)    # Output: False
# Explanation: 'not' inverts the boolean value (True becomes False, and vice versa).

# Combined usage
x = 5
y = 10
print(x > 0 and y < 20)   # Output: True
# Explanation: x > 0 is True and y < 20 is True, so the result is True.

print(x < 0 or y < 20)    # Output: True
# Explanation: x < 0 is False, but y < 20 is True, so 'or' returns True.

print(not (x == 5))       # Output: False
# Explanation: x == 5 is True, so not