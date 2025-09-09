# lambda expressions
# A lambda expression is a small anonymous function that can take any number of arguments,
# but can only have one expression. It is often used for short, throwaway functions that
# are not reused elsewhere.
# Syntax: lambda parameters: expression
def square(x):
    return x * x


# Equivalent lambda expression
square_lambda = lambda x: x * x

# Example usage
print(square(5))  # Output: 25
print(square_lambda(5))  # Output: 25


# Lambda expressions can be used in places where function objects are required, such as in higher-order functions.
# What is higher-order function?
# A higher-order function is a function that takes another function as an argument or returns a function.
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

"""
Rules:
- Single Expression Body: A lambda's body is limited to a single expression. 
  It cannot contain statements like if, for, while, or standard assignment (=). 
  However, you can use expressions that provide conditional logic, like a conditional 
  expression (x if condition else y).
- Any Number of Parameters: A lambda can have zero or more parameters, separated by 
  commas, just like a regular function.
  - lambda: "No params"
  - lambda x: x * 2
  - lambda x, y: x + y
- Implicit Return: The value of the expression is automatically (implicitly) returned. 
  You never use an explicit return statement.
- Statements vs. Expressions
  You cannot use statements like assert or standard assignment (=).
  However, function calls (like print()) are expressions and are technically allowed, 
  but this is often considered poor style as it creates a side effect. The lambda will 
  implicitly return the result of the print() call, which is None. The assignment expression 
  operator (the "walrus operator" :=), introduced in Python 3.8, is allowed within a lambda.

"""
