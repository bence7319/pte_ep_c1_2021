matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
new = []
row = []
for x in range(len(matrix[0])):
    for y in range(len(matrix)-1, -1, -1):
        row.append(matrix[y][x])
    print(row)
    new.append(row)
    row.clear()
"""20, 10, 00, 21, 11, 01, stb."""
