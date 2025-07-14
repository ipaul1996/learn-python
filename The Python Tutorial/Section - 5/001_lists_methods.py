# list.append(x)
# Add an item to the end of the list. Similar to a[len(a):] = [x].
numbers = [1, 2, 3]
numbers.append(4)  # [1, 2, 3, 4]



# list.extend(iterable)
# Extend the list by appending all the items from the iterable. Similar to a[len(a):] = iterable.
numbers.extend([5, 6])  # [1, 2, 3, 4, 5, 6]

# Extending with a tuple
numbers.extend((7, 8))  # [1, 2, 3, 4, 5, 6, 7, 8]

# Extending with a string (adds each character as a separate element)
numbers.extend('90')    # [1, 2, 3, 4, 5, 6, 7, 8, '9', '0']

# Extending with a set (order is not guaranteed)
numbers.extend({11, 12})  # [1, 2, 3, 4, 5, 6, 7, 8, '9', '0', 11, 12]



# list.insert(i, x)
# Insert an item at a given position. The first argument is the index of the element before which to insert, 
# so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
numbers.insert(0, 'start')           # Insert at the beginning: ['start', 1, 2, 3, 4, 5, 6, 7, 8, '9', '0', 11, 12]
numbers.insert(3, 'middle')          # Insert at index 3: ['start', 1, 2, 'middle', 3, 4, 5, 6, 7, 8, '9', '0', 11, 12]
numbers.insert(len(numbers), 'end')  # Insert at the end: [..., 'end']



# list.remove(x)
# Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
numbers.remove('start')   # Removes 'start' from the list
numbers.remove('middle')  # Removes 'middle' from the list
numbers.remove('end')     # Removes 'end' from the list
numbers.remove(1)         # Removes the first occurrence of 1 from the list
# numbers.remove(100)     # ValueError: list.remove(x): x not in list



# list.pop([i])
# Remove the item at the given position in the list, and return it. 
# If no index is specified, a.pop() removes and returns the last item in the list. 
# It raises an IndexError if the list is empty or the index is outside the list range.
last_item = numbers.pop()        # Removes and returns the last item
third_item = numbers.pop(2)      # Removes and returns the item at index 2
# numbers.pop(100)               # IndexError: pop index out of range



# list.clear()
# Remove all items from the list. Similar to del a[:].
numbers.clear()  # numbers is now []



# list.count(x)
# Return the number of times x appears in the list.
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')



# list.copy()
# Return a shallow copy of the list. Similar to a[:].
fruits_copy = fruits.copy()  # fruits_copy is a new list with the same elements as fruits



# list.reverse()
# Reverse the elements of the list in place.
fruits.reverse()           # fruits is now reversed in place
print(fruits)              # Example output: ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

numbers = [1, 2, 3, 4]
numbers.reverse()          # numbers is now [4, 3, 2, 1]



# list.index(x[, start[, end]])
# Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.
# The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular 
# subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
apple_index = fruits.index('apple')            # Returns 1 (first occurrence)
banana_index = fruits.index('banana', 4)       # Returns 6 (search starts at index 4)
# fruits.index('grape')                        # Raises ValueError: 'grape' is not in list



# list.sort(*, key=None, reverse=False)
# The sort() method sorts the list in place.
# key: (optional) a function that serves as a sort key (e.g., key=len to sort by length)
# reverse: (optional) if True, sorts the list in descending order. Default is False (ascending).
numbers = [3, 1, 4, 2]
numbers.sort()  # [1, 2, 3, 4]

# Sorting in reverse order
numbers.sort(reverse=True)  # [4, 3, 2, 1]

# Sorting with a key (by string length)
words = ['banana', 'apple', 'kiwi', 'pear']
words.sort(key=len)  # ['kiwi', 'pear', 'apple', 'banana']

# Sorting a list of tuples by the second element
pairs = [(1, 'one'), (3, 'three'), (2, 'two'), (4, 'four')]
pairs.sort(key=lambda x: x[1])  # [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

# Sorting a list of strings case-insensitively
names = ['alice', 'Bob', 'charlie', 'bob']
names.sort(key=str.lower)  # ['alice', 'Bob', 'bob', 'charlie']

# Sorting a list of numbers as strings
nums = [10, 2, 33, 21]
nums.sort(key=str)  # [10, 2, 21, 33]

# Sorting a list of dictionaries by a specific key
people = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 22}, {'name': 'Dave', 'age': 30}]
people.sort(key=lambda person: person['age'])  # Sorted by age: Jane, John, Dave

# Note: [None, 'hello', 10] doesn’t sort because integers can’t be compared to strings and 
# None can’t be compared to other types. Also, there are some types that don’t have a 
# defined ordering relation. For example, 3+4j < 5+7j isn’t a valid comparison.



# sorted(iterable, *, key=None, reverse=False)
# The sorted() function returns a new sorted list from the items in the iterable.
# It does not modify the original iterable.
# key: (optional) a function that serves as a sort key (e.g., key=len to sort by length)
# reverse: (optional) if True, sorts the list in descending order. Default is False (ascending).
original_list = [3, 1, 4, 2]
sorted_numbers = sorted(original_list)
print(original_list)  # Original list remains unchanged: [3, 1, 4, 2]
print(sorted_numbers)  # Sorted list: [1, 2, 3, 4]
