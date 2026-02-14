# When an exception is created in order to be raised, it is usually initialized with information
# that describes the error that has occurred. There are cases where it is useful to add information
# after the exception was caught. For this purpose, exceptions have a method add_note(note) that
# accepts a string and adds it to the exception’s notes list. The standard traceback rendering includes
# all notes, in the order they were added, after the exception.

try:
    raise TypeError("bad type")
except Exception as e:
    e.add_note("Add some information")
    e.add_note("Add some more information")
    raise
"""
Traceback (most recent call last):
  File "/Users/indrajit.paul/Documents/Code/learn_python/The Python Tutorial/exception_handling/file_005.py", line 8, in <module>
    raise TypeError("bad type")
TypeError: bad type
Add some information
Add some more information
"""