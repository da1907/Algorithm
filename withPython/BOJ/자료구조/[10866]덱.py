import sys
deque = []

for i in range(int(input())):
    command = sys.stdin.readline().strip().split()

    if command[0] == 'push_front':
        deque.insert(0, command[1])     #0번째에 command[1] 값 추가

    elif command[0] == 'push_back':
        deque.insert(len(deque), command[1])    #맨 마지막에 command[1] 값 추가

    elif command[0] == 'pop_front':
        if deque: print(deque.pop(0))
        else: print(-1)

    elif command[0] == 'pop_back':
        if deque: print(deque.pop(len(deque)-1))
        else: print(-1)

    elif command[0] == 'size':
        print(len(deque))

    elif command[0] == 'empty':
        if deque: print(0)
        else: print(1)

    elif command[0] == 'front':
        if deque: print(deque[0])
        else: print(-1)

    elif command[0] == 'back':
        if deque: print(deque[-1])
        else: print(-1)