# range(stop)
# range(start, stop[, step])
# start: The value of the start parameter (or 0 if the parameter was not supplied)
# stop: The value of the stop parameter
# step: The value of the step parameter (or 1 if the parameter was not supplied)
print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(tuple(range(10))) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(list(range(1, 10))) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1, 5, 3)))  # [1, 4]
print(list(range(-10, -100, -30)))  # [-10, -40, -70]


for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4

print() # Line break

for i in range(1, 10, 2):
    print(i, end=" ")  # 1 3 5 7 9

print()  # Line break


# To iterate over the indices of a sequence, we can combine range() and len() as follows:
a = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(a)):
    print(i, a[i])




