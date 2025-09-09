# Defining a function creates a function object and assigns it to a name in the current namespace.
# This name can be used to call the function, and other names can also be assigned to reference the same function object.
# All such names can be used interchangeably to invoke the function.
def greet(name):
    print(f"Hello, {name}!")


# Assign another name to the same function object
say_hello = greet

# Both names can be used to call the function
greet("Alice")
say_hello("Bob")

# Functions that do not include a return statement automatically return a special value called None.
# The return statement is used to exit a function and optionally pass an expression back to the caller.
# If return is used without an expression, or if the end of the function is reached without encountering
# a return statement, None is returned.


def no_return():
    print("This function does not return anything.")


def with_return():
    return 42


def return_none():
    return


def multiple_returns(x):
    if x > 0:
        return "Positive"
    elif x < 0:
        return "Negative"
    else:
        return "Zero"


result1 = no_return()
result2 = with_return()
result3 = return_none()
result4 = multiple_returns(10)
result5 = multiple_returns(-5)
result6 = multiple_returns(0)

print(f"Result of no_return(): {result1}")
print(f"Result of with_return(): {result2}")
print(f"Result of return_none(): {result3}")
print(f"Result of multiple_returns(10): {result4}")
print(f"Result of multiple_returns(-5): {result5}")
print(f"Result of multiple_returns(0): {result6}")
"""
Output:

This function does not return anything.
Result of no_return(): None
Result of with_return(): 42
Result of return_none(): None
Result of multiple_returns(10): Positive
Result of multiple_returns(-5): Negative
Result of multiple_returns(0): Zero
"""

print(type(no_return))  # <class 'function'>
# This confirms that functions themselves are objects, and their type is 'function'.


# A method is a function that belongs to an object, defining a behavior or an action
# that the object can perform. Think of an object as a noun (e.g., a string, a list)
# and a method as a verb (an action). The method is something the object "does".

# You call a method using dot notation: "object.method_name()". This is like
# giving a command: "Tell the object to perform its "method_name" action."

# The methods an object has are defined by its type (its class). Different types can have
# methods with the same name without ambiguity because the method is always called on a
# specific object. You can define your own object types and their corresponding methods by
# writing a class.
