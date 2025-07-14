# In Python, enforcing data hiding is not possible, it is all by convention - anyone can access
# or change it if they want. This means classes can't fully protect their internal data.
# It's up to programmers to follow naming rules and be careful not to break things. You can
# even add new attributes to objects from outside the class, as long as you don't use names
# that the class already uses.


class MyClass:
    def __init__(self, value):
        self.value = value  # public attribute


obj = MyClass(10)
print(obj.value)  # Accessing attribute from outside (allowed)

obj.value = 20  # Modifying attribute from outside (allowed)
print(obj.value)

obj.new_attr = 99  # Adding a new attribute from outside (allowed)
print(obj.new_attr)
