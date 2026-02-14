# With raise,
# Manually trigger an exception when an error or special condition occurs in our code.
# Re-raise an exception caught in an except block to let it propagate further.
# Callers can decide where and how to handle errors (with try/except) rather
# than every function having to manage its own error paths.


def set_age(age: int):
    if not isinstance(age, int):
        raise TypeError(f"age must be int, got {type(age).__name__}")
    if age < 0:
        raise ValueError(f"age must be >= 0, got {age}")
    print(f"Age set to {age}")


# Raising a custom exception
class NegativeBalanceError(Exception):
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise NegativeBalanceError("Withdrawal would result in negative balance!")
    return balance - amount


# Re-raising an exception
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print("Caught division by zero, re-raising...")
        raise


# Raising built-in exceptions with custom messages
def get_item(lst, index):
    if index >= len(lst):
        raise IndexError(f"Index {index} out of range for list of length {len(lst)}")
    return lst[index]


# Example usage:
if __name__ == "__main__":
    try:
        set_age("twenty")
    except Exception as e:
        print(e)

    try:
        withdraw(100, 200)
    except NegativeBalanceError as e:
        print(e)

    try:
        divide(10, 0)
    except ZeroDivisionError as e:
        print(e)

    try:
        get_item([1, 2, 3], 5)
    except IndexError as e:
        print(e)
