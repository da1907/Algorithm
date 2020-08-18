import sys

def solution(stack, x):
    while stack:
        num = stack.pop()
        # num에 저장된 값 여러개일 수 있으므로 모두 탐색해주기 위해
        for i in num:
            if not visited[i]:
                visited[i] = 1
                result[x][i] = 1
                stack.append(child[i])
    return result

n = int(sys.stdin.readline())
matrix = []
stack = []
result = [[0] * n for _ in range(n)]
child = [[]*n for _ in range(n)]

# 한줄씩 입력 받아서 가리키고 있는 노드 child 배열에 저장
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if tmp[j] == 1:
            child[i].append(j)

# 한줄씩 가리키고 있는 노드 stack에 넣어서 solution 함수 호출
for i in range(n):
    visited = [0] * n
    stack.append(child[i])
    result = solution(stack, i)

# 출력
for i in range(n):
    for j in range(n):
        print(result[i][j], end=' ')
    print()
