# setattr
# The setattr() function is a built-in Python function that allows you to dynamically
# set an attribute value on an object. It's particularly useful when you need to set
# attributes whose names are determined at runtime.

# setattr(object, name, value)
# object: The object whose attribute you want to set
# name: A string containing the name of the attribute
# value: The value you want to assign to the attribute


class Person:
    pass


p = Person()
setattr(p, "name", "Alice")
setattr(p, "age", 30)

print(p.name)  # type: ignore # Alice
print(p.age)  # type: ignore # 30


attributes = {"name": "Charlie", "occupation": "Engineer", "city": "Boston"}

for attr, value in attributes.items():
    setattr(p, attr, value)

print(p.occupation)  # type: ignore # Engineer
print(p.city)  # type: ignore  # Boston


# getattr
# The getattr() function is a built-in Python function that allows you to dynamically
# access an object's attributes. It's particularly useful when you need to access attributes
# whose names are determined at runtime.

# getattr(object, name[, default])
# object: The object whose attribute you want to access
# name: A string containing the name of the attribute
# default (optional): The value to return if the attribute doesn't exist


class PersonV2:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = PersonV2("Alice", 30)

# These are equivalent:
print(p.name)  # Alice
print(getattr(p, "name"))  # Alice

# Accessing age
age = getattr(p, "age")
print(age)  # 30

# If the attribute doesn't exist, you can provide a default value
email = getattr(p, "email", "not provided")
print(email)  # not provided

# Without default, it raises AttributeError
# email = getattr(p, 'email')  # This would raise: AttributeError


attributes = ["name", "age", "occupation"]

for attr in attributes:
    value = getattr(p, attr, "N/A")
    print(f"{attr}: {value}")

# Output:
# name: Alice
# age: 30
# occupation: N/A
