# string methods

# upper
s = "Hello World"
print(s.upper())           # 'HELLO WORLD'

# isupper
print(s.isupper())         # False
print(s.upper().isupper()) # True

# lower
print(s.lower())           # 'hello world'

# islower
print(s.islower())         # False
print(s.lower().islower()) # True

# capitalize
s = "hello WORLD"
print(s.capitalize())  # 'Hello world'

# isalpha
# It checks if all characters in the string are alphabetic
# and there is at least one character.
s = "HelloWorld"
print(s.isalpha())  # True

s = "Hello World"
print(s.isalpha())  # False (contains a space)

# isalnum
# It checks if all characters in the string are alphanumeric
# and there is at least one character.
s = "Hello123"
print(s.isalnum())  # True

s = "Hello 123"
print(s.isalnum())  # False (contains a space)



