from itertools import permutations
N, M = map(int, input().split())
arr = []
arr = sorted(list(map(int, input().split())))

for numbers in list(permutations(arr, M)):
    for num in numbers:
        print(num, end = ' ')

    print()