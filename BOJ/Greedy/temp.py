n=int(input())
op=input().split()
check=[False] * 10
mx,mn='',''

def possible(i,j,k):
    if k == '<':
        return i < j
    if k == '>':
        return i > j
    return True  #부등호가 성립하면 true

def solve(cnt, s):
    global mx,mn
    if cnt == n + 1: #숫자개수가 부등호개수보다 1개 많으면
        if not len(mn):
            mn=s
        else:
            print("mx", mx)
            mx=s
            print("mx", mx)
        return
    for i in range(10):
        if not check[i]:
            if cnt == 0 or possible(s[-1],str(i),op[cnt-1]):
                check[i]=True
                print("str",str(i))
                solve(cnt+1, s+str(i)) #dfs탐색
                check[i]=False
solve(0,'')
print(mx)
print(mn)