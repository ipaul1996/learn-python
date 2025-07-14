# del statement
# The del statement can be used to remove items from a list by index or slice.
# It can be used to clear the entire list.
# It can also be used to delete entire variables.
# del numbers[0]  # Removes the first item from the list numbers
# del numbers[1:3]  # Removes the items at index 1 and 2 from the list numbers
# del numbers  # Deletes the entire list numbers
# Referencing the name numbers hereafter is an error (at least until another value is assigned to it). 

numbers = [-1, 1, 66.25, 333, 333, 1234.5]
del numbers[0]
print(numbers)    # [1, 66.25, 333, 333, 1234.5]

del numbers[2:4]
print(numbers)    # [1, 66.25, 1234.5]

del numbers[:]
print(numbers)    # []