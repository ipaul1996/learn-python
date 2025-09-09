# In Python, a decorator is a callable (usually a function) that takes another function or method,
# adds extra behavior to it, and returns a new function with the enhanced behavior.
# Decorators are useful for:
# - Separating concerns: Keep additional logic (like logging, timing, or authentication)
#   out of your core functions.
# - Reusing code: Apply the same wrapper to multiple functions without duplicating code.
# - Improving readability: The @decorator syntax at the function definition makes it clear what
#   modifications are applied.


# A plain function:
def greet(name):
    return f"Hello, {name}!"


# A wrapper function:
# We want to print the time before and after calling greet.
import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, *kwargs)
        end = time.time()

        print(f"{func.__name__} took {end - start:.6f}s")

        return result

    return wrapper


# Applying the decorator
# 1. Manually
greet = timing_decorator(greet)
print(greet("Bob"))

# greet took 0.000001s
# Hello, Bob!


# 2. With @ syntax
@timing_decorator
def greetV2(name):
    return f"Hello, {name}!"


# @timing_decorator is equivalent greet = timing_decorator(greet)
print(greetV2("Robbin"))

# greetV2 took 0.000001s
# Hello, Robbin!
