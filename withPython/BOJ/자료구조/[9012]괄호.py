num = int(input())

for i in range(num):
    vps = list(input())

    while len(vps) != 0:    #vps에 아무것도 없을때까지 반복
        if vps[0] == ')':
            print("NO")
            break

        else:
            if ')' in vps:
                vps.remove(')')
                vps.remove('(')

            else:
                print("NO")
                break

    if len(vps) == 0:
        print("YES")