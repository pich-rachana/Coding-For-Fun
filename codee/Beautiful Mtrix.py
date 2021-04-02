row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
row3 = list(map(int, input().split()))
row4 = list(map(int, input().split()))
row5 = list(map(int, input().split()))

matrix = []
matrix.append(row1)
matrix.append(row2)
matrix.append(row3)
matrix.append(row4)
matrix.append(row5)

positionCol = None
for column in matrix:
    if sum(column) == 1:
        positionCol = matrix.index(column)
        positionRow = column.index(1)

print((abs(positionCol - 2)) + abs(positionRow - 2))