# dictionary
# Dictionaries are mutable(can be changed in-place), unordered collections of key-value pairs.
# dictionaries are indexed by keys, which can be any immutable type;
# (e.g., strings, numbers, tuples(that does not contain mutable objects))
# A pair of braces creates an empty dictionary: {}.
# Placing a comma-separated list of key:value pairs within the braces adds
# initial key:value pairs to the dictionary; this is also the way dictionaries are written on output.

# The main operations on a dictionary are storing a value with some key and extracting the value given the key.
# It is also possible to delete a key:value pair with del. If you store using a key that is already in use,
# the old value associated with that key is forgotten. It is an error to extract a value using a non-existent key.

# Creating dictionaries
empty_dict = {}
person = {"name": "Alice", "age": 30, "city": "New York"}

# Accessing values
print(person["name"])  # 'Alice'

# Adding or updating values
person["email"] = "alice@example.com"
person["age"] = 31  # update

# Deleting a key-value pair
del person["city"]

# Checking if a key exists
if "email" in person:
    print("Email exists")

# get(key[, default])
# Returns the value for key if key is in the dictionary, else returns default.
# If default is not provided, returns None.
print(person.get("age"))  # Returns 31
print(person.get("city"))  # Returns None (since 'city' was deleted)
print(person.get("city", "N/A"))  # Returns 'N/A'
print(person.get("phone", "Not found"))


# Iterating over keys, values, and items
for key in person:
    print(key, person[key])

for value in person.values():
    print(value)

for key, value in person.items():
    print(key, value)

# Getting all keys, values, or items as views
keys = person.keys()
values = person.values()
items = person.items()

# Using enumerate to iterate with index
for idx, key in enumerate(person):
    print(f"{idx}: {key} -> {person[key]}")


# Copying a dictionary (shallow copy)
person_copy = person.copy()

# Removing all items
person.clear()


# pop(key[, default])
# Removes the specified key and returns its value. If key is not found, returns default if given,
# else raises KeyError.
person = {"name": "Alice", "age": 30}
age = person.pop("age")  # returns 30

# popitem()
# Removes and returns a (key, value) pair as a tuple.
item = person.popitem()  # returns ('name', 'Alice')

# Merging dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = {**d1, **d2}  # {'a': 1, 'b': 3, 'c': 4}

# Merging using update()
# update([other])
# Updates the dictionary with key-value pairs from other, overwriting existing keys.
d1.update(d2)  # d1 is now {'a': 1, 'b': 3, 'c': 4}

# fromkeys(seq[, value])
# Creates a new dictionary with keys from seq and values set to value (default is None).
keys = ["a", "b", "c"]
defaults = dict.fromkeys(keys, 0)  # {'a': 0, 'b': 0, 'c': 0}


# Creating a dictionary from a list of tuples
contacts = dict([("sape", 4139), ("guido", 4127), ("jack", 4098)])
print(contacts)

# When the keys are simple strings, you can create a dictionary using keyword arguments:
contacts_kw = dict(sape=4139, guido=4127, jack=4098)
print(contacts_kw)

# Dictionary comprehensions
squares = {x: x * x for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Nested dictionaries
users = {
    "alice": {"age": 30, "email": "alice@example.com"},
    "bob": {"age": 25, "email": "bob@example.com"},
}

# Length of dictionary
print(len(users))  # 2


# Dictionary as function argument (unpacking)
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")


person = {"name": "Charlie", "age": 28}
greet(**person)




