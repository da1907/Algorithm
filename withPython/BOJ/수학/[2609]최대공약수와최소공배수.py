A,B = map(int, input().strip().split())

def gcd(x, y):  #최대공약수
    mod = x % y

    while mod > 0:
        x = y
        y = mod
        mod = x % y
    return y

def lcm(x, y):  #최소공배수
    return x * y // gcd(x, y)

print(gcd(A, B))
print(lcm(A, B))

#유클리드 호제법!!!