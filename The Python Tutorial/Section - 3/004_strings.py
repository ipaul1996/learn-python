# Strings
# A string is a sequence of characters enclosed in quotes.
# Strings are immutable, meaning they cannot be changed after they are created.
print('Hello World!')  # Single quotes
print("Hello World!")  # Double quotes

text = '''This is a
multi-line
string.'''
print(text)
# triple single quotes (''' ... ''') are used to define multi-line strings. We can also use 
# triple double quotes (""" ... """) for the same purpose.
# We can also use it for docstring, which are used to document functions, classes, and modules.
def add(a, b):
    """
    Add two numbers together.

    Parameters:
    a (int | float): The first number.
    b (int | float): The second number.

    Returns:
    int | float: The sum of a and b.
    """
    return a + b

print(add.__doc__)  # Prints the docstring of the add function

# To quote a quote, we need to “escape” it, by preceding it with \. 
# Alternatively, we can use the other type of quotation marks.
print('doesn\'t')
print("doesn't")
print('"Yes," they said.')
print('\"Yes," they said.')
print('"Isn\'t," they said.')

s = 'First line.\nSecond line.'  # \n is a newline character
print(s)  # Prints the string with a newline
s = 'First line.\tSecond line.'  # \t is a tab character
print(s)  # Prints the string with a tab

# If we don’t want characters prefaced by \ to be interpreted as special characters, 
# we can use raw strings by adding an r before the first quote
s1 = r'First line.\nSecond line.'  # Raw string
print(s1)  # First line.\nSecond line.


# f-strings (formatted string literals) allow embedding expressions inside string literals, using {}
# f-strings are evaluated at runtime and can include any valid Python expression
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
# My name is Alice and I am 30 years old.

print(f"In five years, {name} will be {age + 5} years old.")
# In five years, Alice will be 35 years old.

print("In five years, {name} will be {age + 5} years old.")  # This is a regular string, not an f-string
# In five years, {name} will be {age + 5} years old. 


# Both raw and formatted
name = "Alice"
path = rf"C:\Users\{name}\Documents"
print(path)
# Output: C:\Users\Alice\Documents

# String concatenation
print("Hello " + "World!")  # "Hello World!" # String concatenation using the + operator

x = "Prem"
print(x + "Sharma")  # "Prem Sharma"

print("Hello " "World!")  # "Hello World!" # String concatenation using implicit concatenation
# y = x "Kumar"; # SyntaxError: invalid syntax # Implicit concatenation only works with string literals, not variables

# String repetition
print("Spam " * 4)  # "Spam Spam Spam Spam "

# String length
print(len("Hello World!"))  # 12
print(len(x))  # 4

# String indexing
str = "Hello World!"
print(str[0])  # 'H' # First character
print(str[-1])  # '!' # Last character
print(str[-2])  # 'd' # Second last character
print(str[-len(str)])  # 'H' # First character using negative indexing
print(str[len(str) - 1])  # '!' # Last character using length
# print(str[len(str)])  # IndexError: string index out of range

# Indexing overview:
# Positive indices:   0, 1, 2, ..., len(str) - 1
# Negative indices: -len(str), ..., -3, -2, -1
# Both positive and negative indices can be used to access characters in a string.

# String slicing
# Slicing always returns a new string, leaving the original string unchanged.
print(str[0:5])   # characters from position 0 (included) to 5 (excluded) (size of slice = 5 - 0 = 5)
print(str[6:])    # characters from position 6 (included) to the end
print(str[:5])    # characters from position 0 (included) to position 5 (excluded)
print(str[-2:])   # characters from the second-last (included) to the end
print(str[-6:-1]) # characters from the sixth-last (included) to the second-last (excluded)
print(str[:])     # 'Hello World!' # Slicing with no start or end gives the whole string
# Default values for start and end in slicing are 0 and len(str), respectively.

# If the start index is greater than or equal to the end index, an empty string is returned.
print(str[2:2])  # ''
print(str[5:2])  # ''
# This happens because slicing in Python goes from the start index up to, but not including, 
# the end index. If the start index is equal to or greater than the end index, there are no 
# characters to include, so the result is an empty string.

print(str[-25:25]) # Hello World! # No IndexError, it just returns the whole string
# This is because slicing gracefully handles out-of-range indices by adjusting them to 
# fit within the string's bounds, returning as much of the string as possible.

# The start is always included, and the end always excluded. 
# This makes sure that s[:i] + s[i:] is always equal to s.
print(str[:2] + str[2:])  # 'Hello World!' # Concatenation of two slices gives the original string


# Python are immutable. Therefore, assigning to an indexed 
# position in the string results in an error:
# str[0] = 'J' # TypeError: 'str' object does not support item assignment
# If we need a different string, we should create a new one
str = 'J' + str[1:]

