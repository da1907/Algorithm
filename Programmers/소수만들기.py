import itertools
def solution(nums):
    cnt = 0
    can = itertools.combinations(nums, 3)

    for i in can:
        num = sum(i)
        for j in range(2, num):
            if num % j == 0:
                break
        else:
            cnt += 1
    return cnt


nums = list(map(int, input().split()))
solution(nums)