from itertools import combinations
from functools import reduce
def multiply(i):
    return reduce(lambda x, y: x * y, i)

def solution(clothes):
    answer = 1
    checked = []
    li, candidates = [], []
    tmp = 1
    for i in range(len(clothes)):
        cnt = 0
        if clothes[i][1] not in checked:
            for j in range(i, len(clothes)):
                if clothes[i][1] == clothes[j][1]:
                    cnt += 1
            li.append(cnt)
            checked.append(clothes[i][1])

    # for i in range(1, len(li)+1):
    #     for j in list(combinations(li, i)):
    #         if len(j) == 1:
    #             candidates.append(j[0])
    #         else:
    #             candidates.append(multiply(j))
    #     answer += sum(candidates)
    #     candidates.clear()

    for i in li:
        answer *= i+1

    return answer-1

clothes = []
for i in range(5):
    clothes.append(list(input().split( )))

print(solution(clothes))
