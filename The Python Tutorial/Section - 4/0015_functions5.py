# *args and **kwargs
# *args allows a function to accept any number of positional arguments as a tuple.
# **kwargs allows a function to accept any number of keyword arguments as a dictionary.

def demo_args_kwargs(*args, **kwargs):
    print("Positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)

demo_args_kwargs(1, 2, 3, a=4, b=5)
# Output:
# Positional arguments (args): (1, 2, 3)
# Keyword arguments (kwargs): {'a': 4, 'b': 5}

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
Positional arguments (args): (1, 2, 3)
Keyword arguments (kwargs): {'a': 4, 'b': 5}
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
