case = int(input())
nums = list(map(int, input().split()))
cnt = 0
n = 1001
is_prime = [1] * n
is_prime[0], is_prime[1] = 0, 0

m = int(n ** 0.5)
for i in range(2, m + 1):
    if is_prime[i]:
        jmp = 2
        while i * jmp <= 1000:
            is_prime[i*jmp] = 0
            jmp += 1

for t in nums:
    if is_prime[t]:
        cnt += 1

print(cnt)

#에라토스테네스의체 외워놓고 함수로 하나 빼놓고 쓰기
#제곱근 이용하기는 더 큰 범위일때 유용