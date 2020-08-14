N = int(input())
nums = list(map(int, input().split()))

result = [-1] * N
stack = []

stack.append(0)
i = 1

while stack and i < N:
    while stack and nums[stack[-1]] < nums[i]:
        result[stack[-1]] = nums[i]
        stack.pop()
        print(i)

    stack.append(i)
    i += 1

print(result, end = '')