case = int(input())
nums = list(map(int, input().split()))

nums.sort()
sums = [0] * case
for i in range(case):
    for j in range(0, i+1):
        sums[i] += nums[j]

sum = 0
for i in sums:
    sum += i

print(sum)