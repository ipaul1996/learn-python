# tuple - immutable sequence of objects
t1 = 12345, 54321, 'hello!'
t2 = (12345, 54321, 'hello!')
# t1 & t2 are the same

# Tuples may be nested:
t3 = t1, t2, (1, 2, 3, 4, 5)
print(t3) # ((12345, 54321, 'hello!'), (12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# Tuples are immutable:
# t1[0] = 88888  # This will raise a TypeError

# Tuples may contain mutable objects:
t4 = (12345, 54321, ['hello!', 'world!'])
print(t4)  # Output: (12345, 54321, ['hello!', 'world!'])

# An empty tuple,
empty = ()
print(empty)      # Output: ()
print(type(empty))  # Output: <class 'tuple'>

# If we are creating a tuple with one element, we must include a trailing comma:
t5 = (12345)     
print(t5)        # 12345
print(type(t5))  # Output: <class 'int'>

t6 = (12345,)     # This is a tuple with one element
print(t6)        # (12345,)
print(type(t6))  # Output: <class 'tuple'>


# Tuples can be used as dictionary keys:
d = {}
d[t1] = 'demo value'
print(d)  # Output: {(12345, 54321, 'hello!'): 'demo value'}


# Tuple unpacking
x, y, z = t1
print(x)  # Output: 12345
print(y)  # Output: 54321
print(z)  # Output: hello!