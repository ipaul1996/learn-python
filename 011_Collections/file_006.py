from collections import defaultdict


# Example 1: Custom factory that returns an empty list
def list_factory():
    return []


# Using custom factory to group items
groups = defaultdict(list_factory)
# Or you can use the built-in list directly: defaultdict(list)

data = [
    ("fruits", "apple"),
    ("fruits", "banana"),
    ("colors", "red"),
    ("colors", "blue"),
    ("fruits", "orange"),
]

for category, item in data:
    groups[category].append(item)

print(f"\nGrouped data: {groups}")
# defaultdict(<function list_factory at 0x...>, {'fruits': ['apple', 'banana', 'orange'], 'colors': ['red', 'blue']})


# Example 2: Custom factory that returns a default message
def default_message():
    return "No data available"


user_info = defaultdict(default_message)
user_info["name"] = "John"
user_info["age"] = 30

print(f"\nUser name: {user_info['name']}")
print(f"User age: {user_info['age']}")
print(f"User address: {user_info['address']}")  # Will return "No data available"
