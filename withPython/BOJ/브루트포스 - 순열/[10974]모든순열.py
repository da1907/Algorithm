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

N = int(input())        #몇개의 수로 순열 만들지 입력받기
arr = []
num = 1
for i in range(1, N+1):
    arr.append(i)
    print(i, end = ' ')
print()

for i in range(1, N+1):
    num *= i

for i in range(num-1):
    permutation(arr, N)
    print(*arr)