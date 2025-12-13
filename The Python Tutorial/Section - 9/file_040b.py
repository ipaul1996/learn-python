"""
A descriptor is simply any object that defines one or more of these special "magic" methods:

__get__(self, instance, owner)
__set__(self, instance, value)
__delete__(self, instance)

Think of a descriptor as an "agent" or "gatekeeper" for a class attribute. When you assign a descriptor
object to a class attribute, that agent intercepts any attempt to interact with that attribute on instances
of the class.

self: This is the descriptor object itself.

instance: This is the instance of the class whose attribute is being accessed (e.g., the p in p.score).
This is how the descriptor can work with instance-specific data. It will be None if the attribute is
accessed through the class itself (e.g., Player.score).

owner: This is the class that owns the descriptor (e.g., the Player class).

__get__(self, instance, owner)
- Called when you read the attribute's value.
- It should return the calculated or retrieved value for the attribute.

__set__(self, instance, value)
- Called when you try to assign a new value to the attribute (e.g., p4.score = 100).
- It doesn't return anything. Its job is to handle the incoming value, perform validation, and
store it appropriately.

__delete__(self, instance)
- Called when you use the del statement on the attribute (e.g., del p4.score).
- It performs any necessary cleanup.

Data Descriptor: An object that implements __set__ or __delete__. These are "read-write" descriptors.
Data descriptors have the highest lookup priority. If an instance has a data descriptor and an entry
in its own __dict__ with the same name, the data descriptor always wins.

Non-Data Descriptor: An object that only implements __get__. These are "read-only" descriptors. Non-data
descriptors have a lower priority. If an instance has an entry in its __dict__ with the same name,
the __dict__ entry will be used instead of the descriptor.

"""


class NonNegative:
    """A descriptor that ensures an attribute is a non-negative integer."""

    def __set_name__(self, owner, name):
        # This special method is called when the descriptor is created.
        # We'll use it to store the attribute's name (e.g., 'score', 'level').
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        # When we do `p.score`, `instance` is p.
        # We get the value from the instance's internal dictionary.
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        # When we do `p.score = 10`, `instance` is p and `value` is 10.
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        if value < 0:
            raise ValueError("Value must be non-negative")

        # Store the validated value in a "private" variable (e.g., `_score`).
        setattr(instance, self.private_name, value)


class Player:
    # Assign the descriptor object to a class attribute.
    score = NonNegative()
    level = NonNegative()

    def __init__(self, name, initial_score, initial_level):
        self.name = name
        # These assignments will trigger the NonNegative.__set__() method.
        self.score = initial_score
        self.level = initial_level


p = Player("Gandalf", 99, 10)

print(f"{p.name} has a score of {p.score} and a level of {p.level}")
# Gandalf has a score of 99 and a level of 10

# This assignment triggers the __set__ method and its validation
p.score += 1
print(f"New score: {p.score}")
# New score: 100

# This will raise an error thanks to our descriptor's validation
# p.level = -5  # ValueError: Value must be non-negative
