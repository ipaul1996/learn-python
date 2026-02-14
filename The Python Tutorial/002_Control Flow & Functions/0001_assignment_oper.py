# Assignment Operators

a = 2

# Add and assign
a += 3  # Equivalent to: a = a + 3

# Subtract and assign
a -= 5  # Equivalent to: a = a - 5

# Multiply and assign
a *= 5  # Equivalent to: a = a * 5

# Divide and assign (result is always float)
a /= 2  # Equivalent to: a = a / 2

# Floor divide and assign (result is integer division)
a //= 2  # Equivalent to: a = a // 2

# Modulus and assign (assigns remainder)
a %= 3  # Equivalent to: a = a % 3

# Exponentiate and assign (raise to the power)
a **= 2  # Equivalent to: a = a ** 2

"""
Walrus Operator:
In Python, the = operator is only for assignment statements, not expressions.
It doesn't return a value that can be used in comparisons.

while (line = input()) != "quit":
    print(f"Received: {line}")

Thus this gives error. Hence, we have walrus operator.
The := operator (walrus operator), introduced in Python 3.8, allows assignment 
within expressions. It assigns a value to a variable and returns that value, so 
it can be used in comparisons and other expressions.
"""
while (line := input()) != "quit":
    print(f"Received: {line}")
