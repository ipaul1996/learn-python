# @classmethod
# A decorator (@classmethod) that transforms an ordinary method into a method bound
# to the class rather than its instances. Inside a class method, the first parameter
# is conventionally named cls, which refers to the class object itself.
# When calling the class method, class object is implicitly passed as the first argument.
# Since it gets cls, it can read or change class-level attributes.
class MyClass:
    name = "Example"

    @classmethod
    def describe(cls):
        return f"This is {cls.name}"


# You can call the class method directly on the class itself. It implicitly
# receives class object as the first argument.
print(MyClass.describe())  # Output: This is Example

# You can also call the class method on an instance of the class.
# The method still receives the class object(not the instance) as its first argument implicitly.
obj = MyClass()
print(obj.describe())  # Output: This is Example
