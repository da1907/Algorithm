N = int(input())
nums = list(map(int, input().split()))
cnt = []
stack = []
result = [-1] * N

for i in range(N):
    cnt.append((nums[i],nums.count(nums[i])))

stack.append(0)
i = 1

while stack and i < N:
    while stack and cnt[stack[-1]][1] < cnt[i][1]:
        result[stack[-1]] = nums[i]
        stack.pop()

    stack.append(i)
    i += 1

for i in result:
    print(i, end = ' ')

