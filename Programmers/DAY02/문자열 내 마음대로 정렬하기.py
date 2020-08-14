#내가 생각한 답
def solution(strings, n):
    for i in range(len(strings)):
        first = strings[0][n]

        if first > strings[i+1][n]:
            tmp = strings[i]
            strings[i] = strings[i+1]
            strings[i+1] = tmp

        if first == strings[i+1][n]:
            if strings[i] > strings[i+1]:
                tmp = strings[i]
                strings[i] = strings[i + 1]
                strings[i + 1] = tmp

    return strings
#---------------------------
def solution(strings, n):
    #strings를 먼저 사전 순대로 정렬 해준 뒤
    strings = sorted(strings)

    #strings를 정렬하는데 그 기준인 key는 n번째 인덱스의 값을 기준으로 함
    return sorted(strings, key = lambda x : x[n])