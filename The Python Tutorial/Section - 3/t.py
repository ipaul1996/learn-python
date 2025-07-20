squares = [1, 4, 9, 16, 25]

squares[1:3] = [5, 1]
print(squares)  # [1, 5, 1, 16, 25]

squares[1:1] = [0, 0, 0]
print(squares)  # [1, 0, 0, 0, 5, 1, 16, 25]

squares[0:1] = []
print(squares)  # [0, 0, 0, 5, 1, 16, 25]

squares[:] = []
print(squares)

x = 1
y = 5
p = [0, 1, 2, 3, 4, 5, 6, 7, 8]
p[x:y:2] = [-2] * ((y - x) // 2)
print(p)  # [0, -2, 2, -2, 4, 5, 6, 7, 8]
