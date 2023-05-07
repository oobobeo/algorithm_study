# 1010

# mCn
T = int(input())
for _ in range(T):
    n,m = map(int,input().split())
    ans = 1
    for i in range(n+1,m+1):
        ans *= i
    for i in range(1,m-n+1):
        ans //= i
    print(ans)





