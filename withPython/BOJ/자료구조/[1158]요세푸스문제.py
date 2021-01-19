n, k = map(int, input().split())    #n,k 입력 받기
people = [i for i in range(1, n+1)]     #people 리스트에 1번부터 n+1번까지 사람 추가
result = []     #원에서 제거된 사람 리스트
tmp = k-1   #제거될 사람을 가리키게 될 변수(변수는 0부터 시작하므로 입력받은 k값에서 1 빼줘야함)

while True:     #무한 반복
    result.append(people.pop(tmp))  #tmp가 가리키는 사람을 제거해서 result 리스트에 추가

    if not people:
        break   #사람 리스트가 비면 종료

    # 제거될 사람은 원래, (tmp+k)번째의 사람인데 위에서 이미 tmp가 가리키는 사람 한명이 제거되었으므로 1 더 빼준다
    #그런데 그 길이가 남은 사람수를 넘어가는 경우에는, 남은 사람수로 나눈 값의 나머지로
    tmp = (tmp + k - 1) % len(people)

print('<' + ', '.join(map(str, result)) + '>')