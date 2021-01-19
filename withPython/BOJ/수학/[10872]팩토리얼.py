def fac(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    return num * fac(num-1)

print(fac(int(input())))