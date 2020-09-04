import sys
input = sys.stdin.readline

def solution(str, bomb):
    stack = []
    for i in range(len(str)):
        stack.append(str[i])
        cnt = 0

        if len(stack) >= len(bomb):
            for j in range(-1, -1-len(bomb), -1):
                if stack[j] == bomb[j]:
                    cnt += 1
                else:
                    break
            #print(cnt, len(bomb))
            if cnt == len(bomb):
                for i in range(cnt):
                    stack.pop()
    if not len(stack):
        print("FRULA")
    else:
        for i in stack:
            print(i, end='')
    return

str = list(input().strip())
bomb = list(input().strip())

solution(str, bomb)