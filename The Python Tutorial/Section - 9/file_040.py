# Suppose we want a class that holds a non-negative score.


# Implementation: 1
class Player:
    def __init__(self, score):
        self.score = score


# Here nothing stops us from assigning a negative score


class PlayerV2:
    def __init__(self, score):
        self._score = score

    @property
    def score(self):
        """Called when reading p.score"""
        return self._score


# @property is a built-in decorator that lets us define methods
# in a class that can be accessed like attributes.

p2 = PlayerV2(12)
# print(p1.score()) # TypeError: 'int' object is not callable
print(p2.score)  # 12
# When we do p2.score, Python calls Player.score(p2) behind the scenes,
# returning self._score.

# p2.score = 45 # AttributeError: property 'score' of 'PlayerV2' object has no setter


class PlayerV3:
    def __init__(self, score):
        self._score = score

    @property
    def score(self):
        """Called when reading p.score"""
        return self._score

    # Adding Validation with a Setter (@x.setter)
    @score.setter
    def score(self, value):
        if value < 0:
            raise ValueError("Score must be non-negative")
        self._score = value

    # Cleaning Up with a Deleter (@x.deleter)
    @score.deleter
    def score(self):
        print("Deleting score...")
        del self._score


p3 = PlayerV3(5)
print(p3.score)


p3.score = 8
print(p3.score)

# p3.score = -3  # ValueError: Score must be non-negative

del p3.score

# print(p3.score)
# AttributeError: 'PlayerV3' object has no attribute '_score'. Did you mean: 'score'?


# How @property works under the hood:
# When we use @property, @score.setter, and @score.deleter, Python creates a special
# 'property' object and assigns it to our class attribute (e.g., 'score').
#
# This property object manages access to the underlying data by:
# - Using the getter method when we read the attribute (p.score)
# - Using the setter method when we assign to the attribute (p.score = value)
# - Using the deleter method when we delete the attribute (del p.score)

# In summary:
#   p.score         # Calls the getter:   PlayerV3.score.__get__(p3)
#   p.score = 10    # Calls the setter:   PlayerV3.score.__set__(p3, 10)
#   del p.score     # Calls the deleter:  PlayerV3.score.__delete__(p3)

# One property instance holds all three behaviors — getter, setter, deleter — so Python needs
# only that one object in the class dictionary.
# Our public API is p.score, but all logic — validation, computation, cleanup—lives behind the scenes.

print(type(PlayerV3.score))  # <class 'property'>
