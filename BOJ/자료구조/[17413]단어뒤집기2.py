import sys
from collections import deque
q = deque()
stack = []
result = ''
state = True        # 상태 체크위한 변수

str = list(sys.stdin.readline().strip())
for i in str:
    if i == '<':            # '<' 입력 받으면
        while stack:        # 그 전에 stack에 저장되어 있던 것들 결과값에 저장
            result += stack.pop()
        q.append(i)         # '<' 큐에 저장
        state = False       # <, > 안의 문자들은 큐에 저장해야 하므로 상태변수 False로 변경

    elif i == '>':          # '>' 입력 받으면
        q.append(i)         # 큐에 저장
        state = True        # <. > 괄호가 끝났으므로 상태변수 True
        while q:            # 괄호 안에 있던 문자 모두 결과 값에 저장
            result += q.popleft()       # 순서 그대로 나와야 하므로 deque에서 popleft()

    elif i == ' ':          # 공백 입력 받았는데
        if state:           # 괄호 밖의 상태이면
            while stack:    # stack에 저장되어 있는것들 다 결과값에 저장
                result += stack.pop()
            result += ' '   # 공백 전의 문자들을 결과값에 저장해준 뒤 공백 저장
        else:               # <> 괄호 안의 상태이면
            q.append(i)     # 큐에 공백 저장해준 뒤
            while q:        # 큐에 저장되어 있는 문자들을 결과값에 저장
                result += q.popleft()

    else:               # 입력받은 것이 문자이면
        if state:       # 괄호 밖의 상황
            stack.append(i)         # 스택에 저장
        else:           # 괄호 안의 상황
            q.append(i)             # 큐에 저장

while stack:        # 혹시 스택에 남아있는 문자 있다면
    result += stack.pop()       # 모두 결과값에 저장

print(result)
