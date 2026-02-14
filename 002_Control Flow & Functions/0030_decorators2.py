# Decorators with Arguments (The 3-Layer Pattern)


# 1. Layer 1 (The Factory): Accepts the arguments (e.g., 'level').
#    It returns the ACTUAL decorator.
def log_decorator(level):

    # 2. Layer 2 (The Decorator): Accepts the function to be decorated.
    def actual_decorator(func):

        # 3. Layer 3 (The Wrapper): Accepts the runtime arguments of the function.
        def wrapper(*args, **kwargs):
            print(f"[{level}] Running function: {func.__name__}")
            return func(*args, **kwargs)

        return wrapper

    return actual_decorator


# Usage
# The syntax @log_decorator("DEBUG") actually calls the factory first.
@log_decorator("DEBUG")
def add(x, y):
    return x + y


@log_decorator("ERROR")
def divide(x, y):
    return x / y


print(add(2, 3))
# Output:
# [DEBUG] Running function: add
# 5

print(divide(10, 2))
# Output:
# [ERROR] Running function: divide
# 5.0
