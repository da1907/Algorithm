N = int(input())
arr = []
arr = list(map(int, input().split()))

def before(arr):
    for i in range(N-1, -1, -1):
        if i == 0:
            return
        elif arr[i] < arr[i-1]:
            a = i
            break

    for i in range(N-1, a-1, -1):
        if arr[i] < arr[a-1]:
            b = i
            break

    arr[a-1], arr[b] = arr[b], arr[a-1]
    n = N-1
    while a < n:
        arr[a], arr[n] = arr[n], arr[a]
        a += 1
        n -= 1

    return True

if before(arr) is True:
    for i in arr:
        print(i, end = ' ')
    print()
else:
    print(-1)