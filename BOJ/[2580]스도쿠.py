import sys

matrix = []
nine = 0
for i in range(9):
    matrix.append(list(map(int, sys.stdin.readline().strip().split())))
for i in range(9):
    for j in range(9):
        if not matrix[i][j]:
            nine += 1
while nine:
    for i in range(9):
        if matrix[i].count(0) == 1:
            for x in range(1, 10):
                if x not in matrix[i]:
                    key = matrix[i].index(0)
                    matrix[i][key] = x
                    nine -= 1
    for i in range(9):
        li = [j[i] for j in matrix]
        if li.count(0) == 1:
            for x in range(1, 10):
                if x not in li:
                    key = li.index(0)
                    matrix[key][i] = x
                    nine -= 1
    for x in range(0, 7, 3):
        for y in range(0, 7, 3):
            tmp = []
            nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

            for i in range(x, x+3):
                for j in range(y, y+3):
                    if not matrix[i][j]:
                        tmp.append((i, j))
            if len(tmp) == 1:
                for i in range(x, x+3):
                    for j in range(y, y+3):
                        if not matrix[i][j]:
                            tempx, tempy = i, j
                        else:
                            nums.remove(matrix[i][j])
                matrix[tempx][tempy] = nums[0]
                nine -= 1

for i in range(9):
    for j in range(9):
        print(matrix[i][j], end=' ')
    print()
