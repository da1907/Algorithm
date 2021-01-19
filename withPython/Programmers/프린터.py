import sys
input = sys.stdin.readline

def solution(priorities, location):
    arr = []
    num = priorities[location]
    cnt = 0
    if max(priorities) == num:
        return 1
    elif min(priorities) == num and priorities.count(num) == 1:
        return len(priorities)
    else:
        for i in range(len(priorities)):
            arr.append((priorities[i], i))

        while arr:
            val, idx = arr.pop(0)
            priorities.remove(val)
            print(val, idx)
            print(max(priorities))
            if val >= max(priorities):
                cnt += 1
                if idx == location:
                    return cnt
                continue
            else:
                arr.append((val, idx))
                priorities.append(val)

    return cnt

priorities = list(map(int, input().split()))
location = int(input())

print(solution(priorities, location))
