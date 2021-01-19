import sys

queue = []

#입력받는 테스트케이스 수만큼 순회
for i in range(int(sys.stdin.readline())):
    #명령어 입력받기
    arr = sys.stdin.readline().split()
    if arr[0] == 'push':    #push 입력 받으면
        queue.append(arr[1])    #queue 리스트에 두번째 인덱스 인자값 추가
    elif arr[0] == 'pop':   #pop 입력 받으면
        if queue: print(queue.pop(0))   #queue에 값 있으면, 0인덱스 값 pop하고 출력
        else: print(-1)     #queue에 값 없으면, -1 출력
    elif arr[0] == 'size':  #size 입력 받으면
        print(len(queue))   #queue의 길이 출력
    elif arr[0] == 'empty':     #empty 입력 받으면
        if queue: print(0)  #queue에 값 있으면, 0 출력
        else: print(1)  #queue에 값 없으면, 1 출력
    elif arr[0] == 'front':     #front 입력 받으면
        if queue: print(queue[0])   #queue에 값 있으면, 제일 첫 값 출력
        else: print(-1)     #queue에 값 없으면, -1 출력
    elif arr[0] == 'back':  #back 입력 받으면
        if queue: print(queue[-1])  #queue에 값 있으면, 제일 마지막 값 출력
        else: print(-1)     #queue에 값 없으면, -1 출력