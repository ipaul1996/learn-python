"""
# What is a Decorator?
# A decorator is a function that takes another function, "wraps" it with extra behavior,
# and returns the new wrapped function.

# Why use them?
# 1. Separation of Concerns: Keep your core logic clean (e.g., a function just calculates data).
#    Move side tasks (logging, timing, checking permissions) into decorators.
# 2. Reusability: Write the "timing" logic once, apply it to 50 different functions.
# 3. Readability: The @syntax shows exactly what extra behaviors a function has at a glance.
"""

import time

# Step 1: The Decorator Recipe
def timing_decorator(func):
    """
    1. Input: Accepts a function 'func' (The Gift).
    """

    # 2. The Wrapper: Define a new inner function that adds the extra behavior.
    #    We use *args and **kwargs so this wrapper can handle ANY function signature.
    def wrapper(*args, **kwargs):

        # A. Before the function runs (The "Opening" of the gift)
        start_time = time.time()

        # B. Call the original function (Getting the Gift)
        #    We must capture the result so we can return it later.
        result = func(*args, **kwargs)

        # C. After the function runs (The "Cleanup")
        end_time = time.time()
        print(f"Log: {func.__name__} took {end_time - start_time:.6f}s")

        # D. Return the original result (Handing over the gift)
        return result

    # 3. Output: Return the NEW wrapper function (The Wrapped Gift).
    return wrapper


# Step 2: Applying the Decorator (The Manual Way)
def greet(name):
    return f"Hello, {name}!"


# The "Swap":
# We pass 'greet' into the decorator.
# It returns 'wrapper'.
# We overwrite the name 'greet' to point to 'wrapper'.
greet = timing_decorator(greet)

print(greet("Bob"))
# Logic Flow:
# 1. Calls wrapper("Bob")
# 2. wrapper starts timer -> calls original greet("Bob") -> ends timer
# 3. Prints time -> Returns "Hello, Bob!"


# Step 3: Applying the Decorator (The Pythonic Way)

# The @ syntax is just "Syntactic Sugar" for the manual swap above.
# It automatically says: greetV2 = timing_decorator(greetV2)
@timing_decorator
def greetV2(name):
    return f"Hello, {name}!"


print(greetV2("Robbin"))
# Output:
# Log: greetV2 took 0.000001s
# Hello, Robbin!


"""
@my_decorator
def my_func():
    pass
    
Think this as,
my_func = my_decorator(my_func)
my_func points to the code returned by my_decorator.
The returned code is actually a wrapper function of the
actual function my_func with some additional logic.


"""
