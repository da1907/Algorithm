A, B = input().split()

minV = {}

for i in range(len(B) - len(A) + 1):
    cnt = 0
    m = 0
    for j in range(i, i + len(A)):
        if A[m] != B[j]:
            cnt += 1
            m += 1
        else:
            m += 1
    minV[i] = cnt

print(min(minV.values()))
