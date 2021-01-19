sen = list(input())
stack = []
j = 0
num = []

while sen:
    if sen[0] == '+':
        sen.pop(0)
        print(number)
        #stack[j] += number
        print("--", stack)
    elif sen[0] == '-':
        sen.pop(0)
        j += 1
        stack[j] += number
        print(stack)
    else:
        while not(sen[0] == '-' or sen[0] == '+'):
            num.append(sen.pop(0))

        number = int("".join(num))
        stack.append(number)
        print("--",stack)
        print(sen)





