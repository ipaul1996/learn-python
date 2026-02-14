# lambda expressions
# A lambda expression is a small anonymous function that can take any number of arguments,
# but can only have one expression. It is often used for short, throwaway functions that
# are not reused elsewhere.
# Syntax: lambda parameters: expression

"""
Rules:
- Single Expression Body: A lambda is strictly limited to ONE expression
  (a piece of code that evaluates to a value).
  - It CANNOT contain statements (e.g., return, pass, assert, raise).
  - It CANNOT contain blocks (e.g., if/else blocks, for/while loops).
  - It CAN contain conditional expressions (Ternary Operators):
    (value_if_true if condition else value_if_false).

- Any Number of Parameters: A lambda can accept zero, one, or multiple parameters,
  separated by commas (exactly like a standard function).
  - lambda: "No params" (e.g., lambda: print("Hello"))
  - lambda x: x * 2
  - lambda x, y: x + y

- Implicit Return: The result of the single expression is automatically returned.
  You NEVER use the "return" keyword. If the expression evaluates to None
  (like a print call), the lambda returns None.

- Statements vs. Expressions (The strict boundary)
  - Prohibited: You cannot use standard assignment (=) or statements like
    assert, try/except, or del inside a lambda.
  - Allowed (Side Effects): Function calls (like print(), list.append()) are
    expressions, so they are allowed. However, this is often poor style
    because the lambda will return the result of that call (usually None).
  - Allowed (Walrus): The assignment expression operator (:=) IS allowed
    because it returns the assigned value (e.g., lambda x: (y := x + 1)).
"""


def square(x):
    return x * x

# Equivalent lambda expression
square_lambda = lambda x: x * x

# Example usage
print(square(5))  # Output: 25
print(square_lambda(5))  # Output: 25


# Lambda expressions can be used in places where function objects are required, such as 
# in higher-order functions.

# What is higher-order function?
# A higher-order function is a function that takes another function as an argument 
# or returns a function.

# Example: 1 (Takes a function as an argument)
def apply_twice(func, x):
    return func(func(x))

def squareV2(n):
    return n * n

print(apply_twice(squareV2, 2))  # Output: 16

# using lambda
print(apply_twice(lambda n: n * n, 2))  # Output: 16

# ********************************************************


# Example: 2 (Returns a function as its result)
def make_multiplier(n):
    def multiplier(x):
        return x * n

    return multiplier


double = make_multiplier(2)
print(double(5))  # Output: 10

# using lambda
make_multiplierV2 = lambda n: (lambda x: x * n)
double = make_multiplier(2)
print(double(5))  # Output: 10

# ********************************************************
