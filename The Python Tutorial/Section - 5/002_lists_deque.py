# lists as stacks (LIFO/FILO)
stack = [3, 4, 5]

stack.append(6)
stack.append(7)
print(stack) # [3, 4, 5, 6, 7]

print(stack.pop()) # 7
print(stack) # [3, 4, 5, 6]

print(stack.pop()) # 6
print(stack) # [3, 4, 5]


# lists as queues (LILO/FIFO)
# It is also possible to use a list as a queue, where the first element added 
# is the first element retrieved (“first-in, first-out”);
# However, lists are not efficient for this purpose. While appends and pops from 
# the end of list are fast, doing inserts or pops from the beginning of a list is slow 
# (because all of the other elements have to be shifted by one). Thus,
# it is better to use the collections.deque class from the collections module,
# which was designed to have fast appends and pops from both ends.
from collections import deque
queue = deque([3, 4, 5])

queue.append(6)
queue.append(7)
print(queue)           # deque([3, 4, 5, 6, 7])

print(queue.popleft()) # 3
print(queue.popleft()) # 4
print(queue)           # deque([5, 6, 7])
print(list(queue))     # [5, 6, 7]

# Other useful deque methods: appendleft(), pop(), clear()
# extend(iterable): Add all elements from the iterable to the right side.
# extendleft(iterable): Add all elements from the iterable to the left side 
# (note: items are added in reverse order).
# rotate(n=1): Rotate the deque n steps to the right (use negative n to rotate left).