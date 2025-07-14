# A function definition associates the function name with the function object in the current symbol table. 
# The interpreter recognizes the object pointed to by that name as a user-defined function. Other names can 
# also point to that same function object and can also be used to access the function.
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

# A method is a function that ‘belongs’ to an object and 
# is named obj.methodname, where obj is some object, and methodname 
# is the name of a method that is defined by the object’s type. 
# Different types define different methods. Methods of different types may 
# have the same name without causing ambiguity.
# It is possible to define our own object types and methods, using classes.