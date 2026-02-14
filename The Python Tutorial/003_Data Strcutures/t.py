numbers: list[str | int] = [1, 2, 3]

numbers.append(4)

numbers.extend([4, 5])
numbers.extend((7, 8))
numbers.extend({11, 12})

print(numbers)

numbers.insert(0, "start")
numbers.insert(3, "middle")
numbers.insert(len(numbers), "end")

print(numbers)

numbers.remove("end")

squares = [x * x for x in range(10)]
print(squares)

tupList = [(x, y) for x in [1, 2, 3] for y in [3, 2, 5] if x != y]
print(tupList)

vec = [-4, -2, 0, 2, 4]
filtered = [x for x in vec if x >= 0]
print(filtered)  # [0, 2, 4]

squared_vec = [x**2 for x in vec]
print(squared_vec)
