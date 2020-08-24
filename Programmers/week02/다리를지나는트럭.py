from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue=[0]*bridge_length
    answer = 0
    while queue:
        answer += 1
        queue.pop(0)
        if truck_weights:
            if sum(queue) + truck_weights[0] <= weight:
                queue.append(truck_weights.pop(0))
            else:
                queue.append(0)

    return answer

bridge_length = int(input())
weight = int(input())
truck_weights = list(map(int, input().strip().split()))

print(solution(bridge_length, weight, truck_weights))