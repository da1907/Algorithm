import sys
input = sys.stdin.readline

def solution(n):
    result = []
    arr = [1, 2, 4]
    space = 1
    tmp = n
    while 3**space < tmp:
        tmp -= 3**space
        space += 1
    print(tmp,space)

    for i in range(space-1, 0, -1):
        m = tmp // 3**i
        n = tmp % 3**i
        if not n:
            m -= 1
            result.append(arr[m])
            break
        print(m, n)
        result.append(arr[m])
        tmp = n
        print(result)
    for j in range(space - len(result)):
        result.append(arr[n-1])
    answer = ''
    for i in result:
        answer += str(i)
    return int(answer)

num = int(input())
print(solution(num))
