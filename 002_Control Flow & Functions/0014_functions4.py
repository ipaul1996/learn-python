# Positional arguments are matched to parameters in the order they are given.
# Required unless a default value is provided.
def example_function(arg1, arg2, arg3):
    print(f"arg1: {arg1}, arg2: {arg2}, arg3: {arg3}")


example_function(1, 2, 3)  # Positional arguments


# Keyword Arguments matched by the parameter name, not position.
# They can appear in any order after positional arguments.
def func(a, b):
    print(a, b)


func(1, 2)  # 1 2
func(b=2, a=1)  # 1 2

# Positional arguments must come before keyword arguments.
func(1, b=2)  # Valid
# func(a=1, 2)  # Invalid (positional after keyword)

# You cannot provide a value for the same parameter both positionally
# and by keyword.
# func(1, a=2)  # Error: multiple values for argument 'a'
