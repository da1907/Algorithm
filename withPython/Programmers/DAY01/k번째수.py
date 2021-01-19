//도저히 모르겠어서 답 보고 이해

def solution(array, commands):
    result = []

    for command in commands:
        i,j,k = command     #i,j,k 한번에 받을 수 있음
        result.append(sorted(array[i-1:j])[k-1])

    return result