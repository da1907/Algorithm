N = int(input())
arr = []
arr = list(map(int, input().split()))
a, b = 0, 0

#다음 순열 구하는 함수
def next(arr):
    #맨뒤부터 맨처음까지 순회
    for i in range(N-1, -1, -1):
        #결국 아무것도 찾지못하고 맨처음까지 오면 False 반환하고 함수 종료
        if i == 0:
            return False

        #뒷값이 앞값보다 크면
        elif arr[i] > arr[i-1]:
            a = i       #a에 뒷값 해당 인덱스 저장
            break       #반복문 종료

    #맨 뒤부터 a 인덱스까지 순회
    for i in range(N-1, a-1, -1):
        #해당 인덱스의 값이 잘린부분 바로 앞의 수보다 큰 값 찾기
        if arr[i] > arr[a-1]:
            b = i       #찾으면 해당 인덱스 b에 저장
            break       #반복문 종료

    #찾은 잘린 부분에 있는 값과 잘린부분 바로 앞 값 swap
    arr[a-1], arr[b] = arr[b], arr[a-1]

    #n에 배열의 맨 마지막 인덱스값 저장
    n = N-1

    #잘린부분 뒤집어주기
    while a < n:
        arr[a], arr[n] = arr[n], arr[a]
        a += 1
        n -= 1
    return True

#만약 next 함수가 True를 반환하면 배열 출력, False 반환하면 -1 출력
if next(arr) is True:
    for i in arr:
        print(i, end = ' ')
    print()
else:
    print(-1)