# join(iterable)
# Concatenates the elements of an iterable, inserting the string 
# as a separator.
words = ['Hello', 'world']
sentence = ' '.join(words)
print(sentence)  # Output: Hello world

chars = ['a', 'b', 'c']
result = '-'.join(chars)
print(result)  # Output: a-b-c

numbers = [1, 2, 3]
number_str = ', '.join(str(num) for num in numbers)
print(number_str)  # Output: 1, 2, 3


# split(sep=None, maxsplit=-1)
# Splits the string into a list using the specified separator 'sep'.
# If 'sep' is not provided, any whitespace string is a separator.
# The 'maxsplit' argument limits the number of splits (default: -1, which means no limit).
# After 'maxsplit' splits, the rest of the string is returned as the final element.
text = "apple,banana,cherry"
fruits = text.split(',')
print(fruits)  # Output: ['apple', 'banana', 'cherry']

sentence = "The quick brown fox"
words = sentence.split()
print(words)  # Output: ['The', 'quick', 'brown', 'fox']

data = "one:two:three:four"
parts = data.split(':', 2)
print(parts)  # Output: ['one', 'two', 'three:four']


# replace(old, new[, count])
# Returns a new string where all occurrences of the substring 'old' are replaced with 'new'.
# If 'count' is specified, only the first 'count' occurrences are replaced.
text = "banana"
new_text = text.replace("a", "o")
print(new_text)  # Output: bonono

sentence = "one one one"
replaced_sentence = sentence.replace("one", "two", 2)
print(replaced_sentence)  # Output: two two one
