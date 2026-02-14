class MyClass:
    class_attr = 42

    def __init__(self):
        self.instance_attr = 99


obj = MyClass()


def is_instance_attr(obj, attr):
    """Check if attr is an instance attribute of obj."""
    return attr in obj.__dict__


def is_class_attr(obj, attr):
    """Check if attr is a class attribute of obj's class."""
    return attr in type(obj).__dict__


print(
    f"'instance_attr' is instance attribute: {is_instance_attr(obj, 'instance_attr')}"
)
print(f"'class_attr' is instance attribute: {is_instance_attr(obj, 'class_attr')}")
print(f"'class_attr' is class attribute: {is_class_attr(obj, 'class_attr')}")
print(f"'instance_attr' is class attribute: {is_class_attr(obj, 'instance_attr')}")

"""
'instance_attr' is instance attribute: True
'class_attr' is instance attribute: False
'class_attr' is class attribute: True
'instance_attr' is class attribute: False
"""
