# *args(Variable Positional Arguments): Gathers a variable number of positional arguments into a tuple.
# The name "args" is a convention; the asterisk (*) is the crucial syntax.
# It allows a function to be called with more positional arguments than formally defined.

# **kwargs(Variable Keyword Arguments): Gathers a variable number of keyword arguments into a dictionary.
# The name "kwargs" is a convention; the double asterisk (**) is the crucial syntax.
# It allows a function to handle named arguments that it doesn't explicitly define.


def demo_args_kwargs(*args, **kwargs):
    """
    Prints all positional and keyword arguments passed to the function.
    :param args: tuple of positional arguments
    :param kwargs: dict of keyword arguments
    """
    print("Positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)


demo_args_kwargs(1, 2, 3, a=4, b=5)
# Output:
# Positional arguments (args): (1, 2, 3)
# Keyword arguments (kwargs): {'a': 4, 'b': 5}


def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


x = ["Alice", "Hey"]
y = {"name": "Bob", "greeting": "Hi"}

# *x unpacks an iterable (e.g., list, tuple) into positional arguments.
# **y unpacks a mapping (e.g., dict) into keyword arguments.

greet(*x)  # Equivalent to greet("Alice", "Hello")
# Output: Hello, Alice!

greet(**y)  # Equivalent to greet(greeting="Hi", name="Bob")
# Output: Hi, Bob!

"""
If we think demo_args_kwargs(1, 2, 3, a=4, b=5) in the opposite manner:
*args -> 1, 2, 3
args -> (1, 2, 3)

**kwargs -> a=4, b=5
kwargs -> {a: 4, b: 5}
"""


def order_pizza(size, *toppings, **customer_info):
    print(f"Order received for a {size} pizza.")
    if toppings:
        print("Toppings:")
        for topping in toppings:
            print(f" - {topping}")
    else:
        print("No extra toppings.")
    print("-" * 40)
    print("Customer Information:")
    for key, value in customer_info.items():
        print(f"{key.capitalize()}: {value}")


order_pizza(
    "Large",
    "Pepperoni",
    "Mushrooms",
    "Olives",
    name="Alice Smith",
    address="123 Main St",
    phone="555-1234",
)
# The order in which the keyword arguments are printed is guaranteed
# to match the order in which they were provided in the function call.

"""
Output:
Order received for a Large pizza.
Toppings:
 - Pepperoni
 - Mushrooms
 - Olives
----------------------------------------
Customer Information:
Name: Alice Smith
Address: 123 Main St
Phone: 555-1234
"""


"""

* (Single Asterisk)
  - In a function definition (e.g., def my_func(*args)): It packs all extra positional arguments into a single tuple.
  - In a function call (e.g., my_func(*my_list)): It unpacks an iterable (like a list, tuple, string, range object) into separate positional arguments.
  - * on LHS, gather remaining items: a, *remaining = [1, 2, 3, 4] => remaining = (2, 3, 4)
  - * on RHS (inside [] or ()), scatter the items, combined = [*list_a, *list_b]

** (Double Asterisk)
  - In a function definition (e.g., def my_func(**kwargs)): It packs all extra keyword arguments into a single dictionary.
  - In a function call (e.g., my_func(**my_dict)): It unpacks a dictionary into separate keyword arguments.
  - ** on LHS: NOT SUPPORTED. You cannot gather remaining key-value pairs in a standard assignment (e.g., `x, **rest = my_dict` is a SyntaxError).
  - ** on RHS (inside {}), scatters the key-value pairs (Dictionary Merging), combined = {**dict_a, **dict_b}

"""
