def solution(n):
    answer = []
    board = [[0 for _ in range(n)] for _ in range(n)]

    y, x = -1, 0
    number = 1

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                y += 1
            elif i % 3 == 1:
                x += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1

            board[y][x] = number
            number += 1

    for i in range(n):
        for j in range(n):
            if board[i][j]:
                answer.append(board[i][j])
    return answer

print(solution(6))