# lambda expressions
# A lambda expression is a small anonymous function that can take any number of arguments, but can only have one expression.
# It is often used for short, throwaway functions that are not reused elsewhere.
def square(x):
    return x * x

# Equivalent lambda expression
square_lambda = lambda x: x * x

# Example usage
print(square(5))          # Output: 25
print(square_lambda(5))   # Output: 25

# Lambda expressions can be used in places where function objects are required, such as in higher-order functions.
# What is higher-order function?
# A higher-order function is a function that takes another function as an argument or returns a function.
# Example: 1 (Takes a function as an argument)
def apply_twice(func, x):
    return func(func(x))

def square(n):
    return n * n

print(apply_twice(square, 2))  # Output: 16

# using lambda
def apply_twiceV2(func, x):
    return func(func(x))

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







