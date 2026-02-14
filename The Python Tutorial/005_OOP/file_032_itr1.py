# Iterator

# Iterable (The Container): any Python object you can loop over (e.g., list, tuple, string). An iterable
# implements __iter__(), returning an Iterator object.

# Iterator (The Cursor/Bookmark): the object that does the actual stepping through an iterable.
# An iterator must implement two methods:
#   1. __iter__() — returns the iterator object itself.
#   2. __next__() — returns the next item from the sequence. Raises StopIteration exception when no more items.

numbers = [1, 2, 3, 4, 5]

# Obtain an iterator object by calling iter()
# internally calls numbers.__iter__()
itr = iter(numbers)

print("Iterating through the list using an iterator:")
# Use next() to get the next item from the iterator
# internally calls iterator.__next__()
try:
    while True:
        number = next(itr)
        print(number)
except StopIteration:
    print("Reached the end of the iterator.") 

"""
- State: The list (numbers) doesn't change. The iterator (itr) changes state every time you call next().
- One-time use: Iterators are usually "exhaustible." Once you go through them, you cannot reset them. 
  You must create a new iterator from the iterable to loop again.
"""
