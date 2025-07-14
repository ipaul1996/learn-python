# Set
# A set is an unordered collection of unique elements in Python.
# Sets are useful for membership testing, removing duplicates, and performing mathematical set operations
# such as union, intersection, difference, and symmetric difference.
# You can create a set using curly braces, e.g., {1, 2, 3}, or the set() constructor.
# Note: To create an empty set, use set(), not {}. The latter creates an empty dictionary.
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # {'orange', 'banana', 'pear', 'apple'} (Duplicates removed)

print('orange' in basket) # True # fast membership testing

a = set('abracadabra')
b = set('alacazam')

print("Set a (unique letters in 'abracadabra'):", a)
print("Set b (unique letters in 'alacazam'):", b)


print("a - b (difference: letters in a but not in b):", a - b)
print("a | b (union: letters in a or b or both):", a | b)
print("a & b (intersection: letters in both a and b):", a & b)
print("a ^ b (symmetric difference: letters in a or b but not both):", a ^ b)

"""
a - b (difference: letters in a but not in b): {'d', 'b', 'r'}
a | b (union: letters in a or b or both): {'l', 'b', 'a', 'r', 'c', 'z', 'd', 'm'}
a & b (intersection: letters in both a and b): {'a', 'c'}
a ^ b (symmetric difference: letters in a or b but not both): {'l', 'b', 'z', 'm', 'r', 'd'}
"""

# Adding elements to a set
a.add('z')
print("Set a after adding 'z':", a)

# Removing elements from a set
a.remove('z')  # Raises KeyError if 'z' is not present
print("Set a after removing 'z':", a)

# Discarding elements from a set
a.discard('z')  # Does not raise an error if 'z' is not present
print("Set a after discarding 'z':", a)

# Popping an element from a set
popped_element = a.pop()  # Removes and returns an arbitrary element
print("Popped element from set a:", popped_element)
print("Set a after popping an element:", a) 

# Clearing a set
a.clear()  # Removes all elements from the set
print("Set a after clearing:", a)  # Output: set()

# Set comprehensions
squared = {x**2 for x in range(10)}
print("Set of squares from 0 to 9:", squared)
# Set of squares from 0 to 9: {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

even_squares = {x**2 for x in range(10) if x % 2 == 0}
print("Set of squares of even numbers from 0 to 9:", even_squares)
# Set of squares of even numbers from 0 to 9: {0, 64, 4, 36, 16}


