# Membership Operators(in, not in)

# Check if an element exists in a list, tuple, set, or dictionary
lst = [1, 2, 3]
print(2 in lst)     # True
print(1 not in lst) # False

tup = (4, 5, 6)
print(5 in tup)     # True
print(5 not in tup) # False

st = {7, 8, 9}
print(8 in st)      # True
print(8 not in st)  # False

# Check if a key exists in a dictionary
dct = {'a': 1, 'b': 2}
print('a' in dct)       # True
print('a' not in dct)   # False

# Check if a value exists in a dictionary (using .values())
d = {'x': 10, 'y': 20}
print(10 in d.values())  # True

# Check if a substring exists in a string
s = "hello world"
print("world" in s)  # True
print("bye" in s)    # False

