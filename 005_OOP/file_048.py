# Callable Objects: The __call__ Method

# A callable object is any object that you can call using the function-call syntax ().
# While functions and methods are naturally callable, you can make an instance of any class
# callable by implementing the special __call__ method.
# When you write my_object(arg1, arg2), Python translates it into a call to my_object.__call__(arg1, arg2).


class Adder:
    def __init__(self, base):
        self.base = base  # Maintain state

    def __call__(self, value):
        return self.base + value  # Define call behavior


# Create an instance
add_five = Adder(5)

# Call the instance like a function
result = add_five(3)  # Equivalent to add_five.__call__(3)
print(result)  # 8


class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count


# Create a counter instance
counter = Counter()

# Call it multiple times
print(counter())  # Output: 1
print(counter())  # Output: 2
print(counter())  # Output: 3