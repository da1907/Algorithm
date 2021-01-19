import sys

class Stack:
    def __init__(self):
        self.list = []

    def push(self, num):
        self.list.append(num)

    def pop(self):
        if self.size() == 0:
            return -1
        return self.list.pop()

    def top(self):
        return self.list[-1] if self.size != 0 else -1

    def size(self):
        return len(self.list)

    def empty(self):
        return 1 if len(self.list) == 0 else 0

num = int(input())  #몇개의 숫자를 받을것인가
stack = Stack()     #Stack 클래스 사용
inputs = []     #입력 저장하는 list
outputs = []    #출력 저장하는 list


#입력을 받아 inputs 리스트에 저장
for i in range(num):
    inputs.append(int(sys.stdin.readline()))
idx = 0

#출력을 만들기 위해 1부터 순회
for i in range(num):
    stack.push(i+1)
    outputs.append("+")
    print(stack.top())

    while(idx < num and stack.top() == inputs[idx]):
        stack.pop()
        outputs.append("-")
        idx += 1

#stack에 숫자 남아있는 경우 NO 출력
if not stack.empty():
    print("NO")
else:
    for i in outputs:
        print(i)


