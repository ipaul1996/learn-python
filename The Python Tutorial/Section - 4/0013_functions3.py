# We can specify a default value for one or more arguments.
# This creates a function that can be called with fewer arguments
# than it is defined to allow.
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


greet("Alice")  # Uses default greeting
greet("Bob", "Good morning")  # Uses custom greeting


def power(base, exponent=2):
    return base**exponent


print(power(3))  # Uses default exponent (prints 9)
print(power(2, 5))  # Uses custom exponent (prints 32)

# Default argument values are set when the function is defined, not when it is called.
i = 5

def f(arg=i):
    print(arg)

i = 6
f()
# The output will be 5, not 6, because the default value of `arg` was set
# to the value of `i` when the function `f` was defined.


# This means that if a mutable object (like a list or dictionary) is used as a default value,
# it will be shared across all calls to the function that use that default value.
def append_to_list(value, lst=[]):
    lst.append(value)
    return lst

print(append_to_list(1))        # [1]
print(append_to_list(2))        # [1, 2]
print(append_to_list(3, []))    # [3] (new list, does not share with previous calls)
print(append_to_list(4))        # [1, 2, 4] (shares the default list)


# To avoid this, you can use None as a default value and create a new list inside the function if needed.
def append_to_list_safe(value, lst=None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst

print(append_to_list_safe(1))      # [1]
print(append_to_list_safe(2))      # [2] (new list, does not share with previous calls)
print(append_to_list_safe(3, []))  # [3] (new list, does not share with previous calls)
print(append_to_list_safe(4))      # [4] (new list, does not share with previous calls)


