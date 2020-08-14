import sys

def check(x):
    start = 0
    end = len(arr)-1
    mid = (start+end) // 2
    while start <= end:
        if arr[mid] < x:
            start = mid+1
        else:
            end = mid-1
    return start

n = int(sys.stdin.readline())
port = list(map(int, sys.stdin.readline().split()))
#check = [0] * n
maxV = 0
arr = [port[0]]

for i in range(1, n):
    if arr[-1] < port[i]:
        arr.append(port[i])
        print("1", arr)
    else:
        if arr[0] < port[i]:
            arr.pop(0)
            arr.insert(0, port[i])
            #arr[0] = port[i]
            print("2", arr)
        else:
            #check(port[i])
            arr.insert(check(port[i]), port[i])
            print("3", arr)

print(arr)
print(len(arr))
