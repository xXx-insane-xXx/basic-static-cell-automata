cells = [
    [0, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
]


for row in range(len(cells)):
    for col in range(len(cells[row])):
        if (col != 3):
            if (cells[row][col+1] == 1 or cells[row][col-1] == 1):
                cells[row][col] = 1
            else:
                cells[row][col] = 0

        else:
            if (cells[row][0] == 1 or cells[row][col-1] == 1):
                cells[row][col] = 1
            else:
                cells[row][col] = 0

for i in cells:
    for j in i:
        print(j, end=" ")
    print()
