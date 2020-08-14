M, N = map(int, input().split())
prime = []
n = 1000001
m = int(n ** 0.5)
is_prime = [1] * n
is_prime[0], is_prime[1] = 0, 0

for i in range(2, m + 1):
    if is_prime:
        jmp = 2
        while i * jmp < n:
            is_prime[i * jmp] = 0
            jmp += 1

for i in range(M, N+1):
    if is_prime[i]:
        prime.append(i)

for i in range(len(prime) - 1):
    print(prime[i])

print(prime[-1], end = '')