# The Problem: Uncontrolled Attribute Access
# Suppose we want a Player class that holds a score, which must always be non-negative.


# Approach - 1
class Player:
    def __init__(self, score):
        # This is a public attribute. Anyone can change it to anything.
        self.score = score


p1 = Player(50)
p1.score = -10  # This is allowed, but it breaks our rule!

# The problem here is direct access. Nothing stops a user from assigning an invalid value to score.
# We need a way to intercept access to this attribute to enforce our rules.

# The Solution: Using @property to Create a "Managed Attribute"
# The @property decorator lets us turn a class method into a "virtual attribute." This provides a public,
# attribute-like API (p.score) while running our custom logic behind the scenes. This approach is often
# called creating a "managed attribute." The core idea is to use an internal variable (by convention, prefixed
# with an underscore like _score) to store the actual data and use the property to manage access to it.

# Step 1: The Getter — Creating a Read-Only Attribute


class PlayerV2:
    def __init__(self, score):
        # '_score' is our internal variable.
        # The single underscore is a strong convention in Python
        # indicating it's not meant for direct external access.
        self._score = score

    @property
    def score(self):
        """This is the 'getter' method. It's called when we read `p.score`."""
        print("Getting score...")
        return self._score


p2 = PlayerV2(12)

# Accessing p2.score now calls the score() method automatically.
# Notice we don't use parentheses like a method call.
print(p2.score)
# Getting score...
# 12

# But we can't change it yet! This creates a read-only property.
# p2.score = 45  # Raises AttributeError: property 'score' has no setter

# Step 2: The Setter — Adding Validation Logic
# To allow modification and add validation, we define a "setter" method. The decorator for the setter
# is named after the getter method (@score.setter).


class PlayerV3:
    def __init__(self, score):
        self._score = score

    @property
    def score(self):
        """The GETTER: Called when reading p.score"""
        return self._score

    @score.setter
    def score(self, value):
        """The SETTER: Called when assigning to p.score (e.g., p.score = 10)"""
        if not isinstance(value, int):
            raise TypeError("Score must be an integer")
        if value < 0:
            raise ValueError("Score must be non-negative")
        print(f"Setting score to {value}...")
        self._score = value


p3 = PlayerV3(5)
print(p3.score)  # Calls the getter -> 5

# This assignment now calls the setter method, which validates the input.
p3.score = 8
# Setting score to 8...
print(p3.score)  # Calls the getter -> 8

# The setter's validation logic prevents invalid assignments.
# p3.score = -3  # Raises ValueError: Score must be non-negative
# p3.score = "abc" # Raises TypeError: Score must be an integer


# Step 3: The Deleter — Adding Custom Cleanup Logic
# Finally, you can define a "deleter" to run custom logic when the attribute is deleted with the del keyword.


class PlayerV4:
    def __init__(self, score):
        self.score = score  # The initial assignment also uses the setter!

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if value < 0:
            raise ValueError("Score must be non-negative")
        self._score = value

    @score.deleter
    def score(self):
        """The DELETER: Called when running `del p.score`"""
        print("Deleting score...")
        del self._score


p4 = PlayerV4(100)
del p4.score
# Deleting score...

# Now the internal '_score' attribute is gone.
# print(p4.score)  # Raises AttributeError: 'PlayerV4' object has no attribute '_score'

"""
How It Works Under the Hood: The Descriptor Protocol
When you use these decorators, Python creates a single property object and assigns it to the score 
attribute of the class. This object is a descriptor, which is a special type of object that knows how 
to manage attribute access.

A descriptor works by implementing special methods:
- __get__(): Controls what happens when you read the attribute.
- __set__(): Controls what happens when you assign to the attribute.
- __delete__(): Controls what happens when you delete the attribute.

The @property, @*.setter, and @*.deleter decorators are just convenient syntax for creating this property 
object and attaching your getter, setter, and deleter functions to its __get__, __set__, and __delete__ behaviors.

# The 'score' attribute on the class itself is a property object
print(type(PlayerV4.score))
# >> <class 'property'>

# In summary, your simple attribute access is translated behind the scenes:
# p.score       -> Calls the getter:   PlayerV4.score.__get__(p)
# p.score = 10  -> Calls the setter:   PlayerV4.score.__set__(p, 10)
# del p.score   -> Calls the deleter:  PlayerV4.score.__delete__(p)

"""
