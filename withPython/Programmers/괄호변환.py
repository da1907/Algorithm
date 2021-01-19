def recur(u):
    stack = []
    if not u:
        return

    for i in range(len(u)):
        if u[i] == '(':
            stack.append(u[i])
        else:
            if not stack:



def solution(p):
    answer = ''

    u, v = [], []
    p = list(p)

    u.append(p.pop(0))


    while True:
        print("DDD")

        if u.count('(') == u.count(')'):
            break

        u.append(p.pop(0))

    v = p

    print(u, p)



    return answer

p = '()))((()'
print(solution(p))