import sys
case = int(input())

arr = []
stack = []

for i in range(case):
    #한줄씩 받아온다
    arr.append(sys.stdin.readline().strip().split())

    #arr에 저장된 첫 문자열이 push이면
    if(arr[i][0] == 'push'):
        arr[i][1] = int(arr[i][1])  #int형으로 바꿔주고
        stack.append(int(arr[i][1]))    #스택 배열에 추가

    elif(arr[i][0] == 'top'):
        if (len(stack) == 0): print(-1)     #스택이 비어있으면(=길이가 0이면) -1 출력
        else:   #비어있는게 아니면
            print(stack[-1])    #stack의 마지막 요소 출력

    elif(arr[i][0] == 'size'):
        print(len(stack))

    elif(arr[i][0] == 'empty'):
        if(len(stack) == 0): print(1)   #스택 비어있으면 1 출력
        else: print(0)  #비어있는게 아니면 0 출력

    else:
        if (len(stack) == 0): print(-1)     #stack 비어 있으면 -1 출력
        else:
            print(stack.pop())  #pop 한 뒤 그 값 출력

#웬만한 자료구조들의 함수는 시간복잡도 O(1)