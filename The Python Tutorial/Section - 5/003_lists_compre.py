# List Comprehensions
# List comprehensions provide a concise way to create lists.
# It consists of brackets containing an expression followed by a for clause,
# then zero or more for or if clauses.
# The result will be a new list resulting from evaluating the expression in the context of the for
# and if clauses that follow it.

# Let's create a list of squares:
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

tupList = [(x, y) for x in [1, 2, 3] for y in [3, 2, 5] if x != y]
print(tupList)  # [(1, 3), (1, 2), (1, 5), (2, 3), (2, 5), (3, 2), (3, 5)]

# To create a list of squares of even numbers:
squares_of_evens = [x**2 for x in range(10) if x % 2 == 0]
print(squares_of_evens)  # [0, 4, 16, 36, 64]

vec = [-4, -2, 0, 2, 4]
# filter the above list to exclude negative numbers
filtered = [x for x in vec if x >= 0]
print(filtered)  # [0, 2, 4]


# Apply a function to each element in a list
def square(x):
    return x * x


squared_vec = [square(x) for x in vec]
print(squared_vec)  # [16, 4, 0, 4, 16]

# call a method on each element
fresh_fruit = ["  banana", "  loganberry ", "passion fruit  "]

cleaned_fruit = [fruit.strip() for fruit in fresh_fruit]
print(cleaned_fruit)  # ['banana', 'loganberry', 'passion fruit']

# Flatten a list of lists
vec_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for subList in vec_of_lists for item in subList]
print(flattened) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
