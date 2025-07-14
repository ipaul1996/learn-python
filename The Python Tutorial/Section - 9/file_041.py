# In Python, an object doesn't need to belong to a specific class or inherit from a particular interface to be used in a given context.
# This is called "duck typing": if an object implements the required methods or attributes, it can be used as needed.
# - Avoid isinstance checks: Don't ask "Is this a Duck?"—just use the object as needed.
# - Prefer EAFP (Easier to Ask Forgiveness than Permission): Try to use the object's methods/attributes directly and
#   handle exceptions if they don't exist.
class Duck:
    def quack(self):
        print("Quack!")


class Person:
    def quack(self):
        print("I'm pretending to be a duck!")


def make_it_quack(thing):
    # We don’t check isinstance(thing, Duck)
    thing.quack()


# EAFP
def make_it_quack_v2(thing):
    try:
        thing.quack()
    except AttributeError:
        print("This one can’t quack!")


make_it_quack(Duck())  # Quack!
make_it_quack(Person())  # I'm pretending to be a duck!
