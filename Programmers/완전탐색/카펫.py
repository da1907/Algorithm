def solution(brown, yellow):
    arr = []
    answer = []
    if yellow == 1:
        answer = [3, 3]
    for i in range(1, yellow//2 + 1):
        if (yellow%i == 0):
            if(i > yellow//i):
                break
            arr.append((yellow//i, i))

    for i in arr:
        if ((i[0] + 2 + i[1]) * 2) == brown :
            answer.append(i[0] + 2)
            answer.append(i[1] + 2)

    return answer

brown, yellow = map(int, input().split())
print(solution(brown, yellow))