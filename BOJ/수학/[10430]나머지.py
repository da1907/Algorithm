A, B, C = map(int, input().strip().split())

print((A + B) % C)
print((A % C + B % C) % C)
print((A * B) % C)
print((A % C * B % C) % C)