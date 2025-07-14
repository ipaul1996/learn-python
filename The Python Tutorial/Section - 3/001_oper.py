print("Hello World!")
print("Any", "number", "of", "arguments")

# Comment

# integer number has type int and decimal number has type float
x = 10
y = 3.14

# Arithmetic operators: +, -, *, / (returns a float), // (integer division/floor division) (returns an int),
# % (Modulo), ** (Exponentiation)
a = 7
b = 3

print("Addition:", a + b)  # Addition
print("Subtraction:", a - b)  # Subtraction
print("Multiplication:", a * b)  # Multiplication
print("Division:", a / b)  # Division # (always returns float)
print(
    "Floor Division:", a // b
)  # Floor Division / Integer Division # (always returns int)
print("Modulus:", a % b)  # Modulus
print("Exponentiation:", a**b)  # Exponentiation


# Unary operators: + (positive) and - (negative)
l = 7
t = -l  # Negation
print("Negation of l:", t)  # Output: -7


# Python supports floating point arithmetic. When using operators with mixed types (int and float),
# the integer is automatically converted to a float:
result = 4 * 3.75 - 1
print("Result of 4 * 3.75 - 1.5:", result)  # Output: 14.0

# Python also supports complex numbers, which are represented as a + bj,
# where a is the real part and b is the imaginary part.
complex_number = 3 + 4j
print(complex_number)  # Output: (3+4j)


# Arithmetic Operator precedence:
# **
# unary +/-
# *, /, //, %
# +, -
