# try: Wrap code that may raise exceptions.
# except: Catch and handle specific exceptions.
# else: Run only if no exception occurred in the try.
# finally: Run always, regardless of exceptions, for cleanup.

# Flow: try → except* → else → finally

# If there is an unhandled exception, finally will execute, then the exception will propagate up.
# finally is used to release resources(files, sockets). It executes even if you return or raise inside try or except.

# If there is a try we must have at least one of: except, finally, or both.
# The else block is optional and must come after all except blocks (if present), but before finally.
"""
try:
    do_something()
except ValueError:
    handle_value_error()
except (TypeError, KeyError) as e:
    log_and_handle(e)
except Exception as e:
    generic_handler(e)
else:
    proceed_when_no_error()
finally:
    cleanup_resources()

"""


def intensive_calc(data: dict) -> float:
    """
    Performs division using values from a dictionary.

    Args:
        data (dict): A dictionary containing 'numerator' and 'denominator' keys with numeric values.

    Returns:
        float: The result of dividing 'numerator' by 'denominator'.

    Raises:
        KeyError: If 'numerator' or 'denominator' keys are missing in the dictionary.
        ZeroDivisionError: If the denominator is zero.
        TypeError: If the values are not numbers.
    """
    num = data["numerator"]
    den = data["denominator"]
    return num / den


def compute(data: dict):
    try:
        result = intensive_calc(data)
    except ZeroDivisionError as e:
        return f"Error: {e}"
    else:
        return result * 2
    finally:
        print("compute() completed")


input1 = {"numerator": 10, "denominator": 2}
output1 = compute(input1)
print("Output1", output1)

"""
compute() completed
Output1 10.0
"""

print("********************")

input2 = {"numerator": 5, "denominator": 0}
output2 = compute(input2)
print("Output2", output2)

"""
compute() completed
Output2 Error: division by zero
"""
