#다음 순열 구하는 함수
def permutation(arr, N):
    for i in range(N-1, -1, -1):
        if i == 0:
            return False
        elif arr[i] > arr[i-1]:
            a = i
            break

    for i in range(N-1, a-1, -1):
        if arr[i] > arr[a-1]:
            b = i
            break

    arr[a-1], arr[b] = arr[b], arr[a-1]

    n = N-1

    while a < n:
        arr[a], arr[n] = arr[n], arr[a]
        a += 1
        n -= 1

    return arr

N = int(input())    #몇개의 수로 할것인가
arr = []
next_permu = []
arr = sorted(list(map(int, input().split())))       #순열 할 배열 받아오기

num = 1
sum, ans = 0, 0

#순열의 종류는 N! 개
for i in range(1, N+1):
    num *= i

#맨 처음은 정렬된 배열로 시작
for i in range(num):
    sum = 0
    for j in range(N-1):    #리스트 내의 수끼리 뺀 값의 절대값 sum에 더해줌
        sum += abs(arr[j]-arr[j+1])
    ans = max(ans, sum)     #최대값 갱신
    permutation(arr, N)     #다음 순열로 리스트 바꿔주기

print(ans)

