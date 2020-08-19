from collections import deque

def solution(progresses, speeds):
    days = [0] * len(progresses)
    queue = deque()
    result = []

    # 남은 날짜 계산
    for i in range(len(progresses)):
        if not (100-progresses[i]) % speeds[i]:
            days[i] = (100-progresses[i]) // speeds[i]
        else:
            days[i] = ((100-progresses[i]) // speeds[i]) + 1

    # queue에 넣다가 다음 들어올 수가 queue[0]보다 크면
    # 현재 queue에 있는 모든 수 pop해주면서 몇개 pop 했는지 count 해서
    # result 배열에 넣어준다
    queue.append(days[0])
    for i in range(1, len(days)):
        if queue[0] < days[i]:
            cnt = 0
            while len(queue):
                queue.popleft()
                cnt += 1
            result.append(cnt)
            queue.append(days[i])
        else:
            queue.append(days[i])

    # 더이상 큰 수가 들어오지 않아서 queue에 수가 남은채로 끝나면
    # 남은 수들 모두 배포해주기 위해 queue에 몇개 남았는지 count
    if len(queue):
        result.append(len(queue))

    return result

progresses = list(map(int, input().split()))
speeds = list(map(int, input().split()))

print(solution(progresses, speeds))