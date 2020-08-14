from sys import stdin

for sen in stdin:
    cnt = [0] * 4

    for i in sen:
        if i.islower():
            cnt[0] += 1
        elif i.isupper():
            cnt[1] += 1
        elif i.isdigit():
            cnt[2] += 1
        else:
            cnt[3] += 1

    cnt[3] -= 1
    print(*cnt)


