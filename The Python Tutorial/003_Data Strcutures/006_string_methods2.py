# string methods

# center(width[, fillchar])
# Returns a centered string of length width. Pads with fillchar (default is space) on both sides.
s = "Hello"
print(s.center(20))          # '       Hello        '
print(s.center(20, '*'))     # '*******Hello********'

# count(sub[, start[, end]])
# Returns the number of non-overlapping occurrences of substring sub in the string.
# start(included) and end (excluded) are optional parameters that specify the range within which to count.
s = "Helloooo Woorld"
print(s.count('o'))          # 6
print(s.count('oo'))         # 3 (not 4 --> No overlapping is counted)
print(s.count('o', 0, 5))    # 1 


# endswith(suffix[, start[, end]])
# Returns True if the string ends with the specified suffix (optionally within start(included) and end(excluded)).
s = "Hello, world!"
print(s.endswith('!'))             # True
print(s.endswith('world!'))        # True
print(s.endswith('Hello'))         # False
print(s.endswith('o', 0, 5))       # True (checks if s[0:5] ends with 'o')
print(s.endswith(('!', '?')))      # True (checks if ends with any of the tuple elements)

# startswith(prefix[, start[, end]])
# Returns True if the string starts with the specified prefix (optionally within start(included) and end(excluded)).
s = "Hello, world!"
print(s.startswith('Hello'))         # True
print(s.startswith('world'))         # False
print(s.startswith('H'))             # True
print(s.startswith('e', 1))          # True (checks if s[1:] starts with 'e')
print(s.startswith(('Hello', 'Hi'))) # True (checks if starts with any of the tuple elements)

# strip([chars])
# Returns a copy of the string with leading and trailing characters removed (default: whitespace).
s = "   Hello, world!   "
print(s.strip())                # 'Hello, world!'

s = "---Hello---"
print(s.strip('-'))             # 'Hello'

s = "xyxHello,xyx"
print(s.strip('xy'))            # 'Hello,'


# find(sub[, start[, end]])
# Returns the lowest index where substring sub is found, or -1 
# if not found (optionally within start(included) and end(excluded)).
s = "Hello, world!"
print(s.find('world'))        # 7
print(s.find('o'))            # 4 (first occurrence)
print(s.find('o', 5))         # 8 (search starts from index 5)
print(s.find('Python'))       # -1 (not found)
print(s.find('l', 3, 7))      # 3 (searches in s[3:7], finds 'l' at index 3)


# index(sub[, start[, end]])
# Like find(), but raises a ValueError if the substring is not found.
s = "Hello, world!"
print(s.index('world'))        # 7
print(s.index('o'))            # 4 (first occurrence)
print(s.index('o', 5))         # 8 (search starts from index 5)
# print(s.index('Python'))     # Uncommenting this line will raise ValueError: substring not found
print(s.index('l', 3, 7))      # 3 (searches in s[3:7], finds 'l' at index 3)
