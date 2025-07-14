# 'for'
# The 'for' statement iterates over the items of any sequence (like lists, tuples, 
# strings, or dictionaries) in the order they appear.

# Example: Iterating over a list
words = ["hello", "world", "python", "rocks"]

for word in words:
    print(word, len(word))  # Prints each word and its length

for word in words:
    print(word.upper(), end="😘 ")  # Prints each word in uppercase, separated by a custom emoji

# Using enumerate() to get index and value while iterating
for index, word in enumerate(words):
    print(f"Word at index {index} is {word}")

# Example: Iterating over a tuple
animals = ("cat", "dog", "rabbit", "hamster")

for animal in animals:
    print(animal)  # Prints each animal

# Example: Using range() to iterate over a sequence of numbers
for i in range(8):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")

# Example: Iterating over a string
for char in "Python":
    print(char, end=" ")  # Prints each character in the string

# Working with dictionaries
users = {"Hans": "active", "Éléonore": "inactive", "景太郎": "active"}

# keys() --> Returns a view object displaying a list of all the keys in the dictionary.
print(users.keys())    # dict_keys(['Hans', 'Éléonore', '景太郎'])

# values() --> Returns a view object displaying a list of all the values in the dictionary.
print(users.values())  # dict_values(['active', 'inactive', 'active'])

# items() --> Returns a view object displaying a list of the dictionary’s key-value pairs as tuples.
print(users.items())   # dict_items([('Hans', 'active'), ('Éléonore', 'inactive'), ('景太郎', 'active')])

# These view objects are dynamic—if the dictionary changes, the views update automatically.
# These views are not lists, but they can be converted to lists if needed using the `list()` function.
# The 'for' statement can be used to iterate over these view objects.

# Iterating over dictionary keys
for key in users.keys():
    print(key, type(key))

# Iterating over dictionary values
for value in users.values():
    print(value, type(value))

# Iterating over dictionary items (key-value pairs)
for item in users.items():
    print(item, type(item))
    key, value = item
    print("Key is", key, "and value is", value)

# Note:
# Modifying a collection while iterating over it can lead to unexpected behavior.
# To avoid issues, iterate over a copy or build a new collection.

# Strategy 1: Iterate over a copy to safely modify the original dictionary
for user, status in users.copy().items():
    if status == "inactive":
        del users[user]

# Strategy 2: Build a new collection with only the desired items
active_users = {}
for user, status in users.items():
    if status == "active":
        active_users[user] = status

