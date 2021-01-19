import heapq
def solution(scoville, k):
    # 1
    answer = 0
    heapq.heapify(scoville)

    # 2
    while scoville[0] < k:

        # 3
        result = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, result)
        answer += 1

        # 4
        if len(scoville) == 1 and scoville[0] <k:
            return -1
    # 5
    return answer

scoville = list(map(int, input().split()))
k = int(input())
print(solution(scoville, k))