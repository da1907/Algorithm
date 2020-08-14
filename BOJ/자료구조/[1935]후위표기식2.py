# 피연산자 만나면 push, 연산자 만나면 pop

N = int(input())    # 피연산자의 개수
sen = input()       # 후위 표기식
alpha = [0] * N     # 피연산자에 대응하는 값 받을 리스트 선언

for i in range(N):
    alpha[i] = int(input())     # 피연산자에 대응하는 값 받기

stack = []      # 스택 선언

for i in sen:
    if 'A' <= i <= 'Z':     # 피연산자 만나면
        stack.append(alpha[ord(i) - ord('A')])      # 스택에 저장
    else:       # 연산자이면
        str2 = stack.pop()      # 스택에 저장되어 있던 피연산자 두개 pop
        str1 = stack.pop()

        if i == '+':
            stack.append(str1 + str2)
        elif i == '-':
            stack.append(str1 - str2)
        elif i == '*':
            stack.append(str1 * str2)
        elif i == '/':
            stack.append(str1 / str2)

# 마지막에 스택에 남아있는 값 소수점 둘째자리까지 출력
print('%.2f' %stack[0])