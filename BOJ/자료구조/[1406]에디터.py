import sys

#왼쪽 스택과 오른 스택을 만들어서 왼스택에 문자열 저장
l_stk = list(sys.stdin.readline().strip())
r_stk = []

#테스트 케이스 입력받기
test = int(input())

#테스트 케이스만큼 순회
for i in range(test):
    #command에 문자열 입력 받기
    command = sys.stdin.readline().strip().split()
    if command[0] == 'L':   #L 입력 받으면
        if l_stk: r_stk.append(l_stk.pop())     #왼스택에 문자 있을때, 오른스택으로 왼스택의 제일 윗값 옮기기
        else: continue  #왼스택에 문자 없으면 넘어감(무시)
    elif command[0] == 'D':     #D 입력 받으면
        if r_stk: l_stk.append(r_stk.pop())     #오른스택에 문자 있으면, 왼스택으로 오른스택의 제일 윗값 옮기기
    elif command[0] == 'B':     #B 입력 받으면
        if l_stk: l_stk.pop()   #왼스택에 문자 있으면, 왼스택 제일 윗값 지워줌
        else: continue  #왼스택에 문자 없으면, 넘어감(무시)
    elif command[0] == 'P':     #P 입력 받으면
        l_stk.append(command[1])    #왼스택의 제일 마지막에 두번째 인덱스 해당하는 값 추가해줌

print(''.join(l_stk + list(reversed(r_stk))))   #왼스택과 오른스택을 거꾸로한 것을 더해서 출력
