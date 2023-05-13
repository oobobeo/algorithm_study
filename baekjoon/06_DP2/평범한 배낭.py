# 12865

'''
동전바꿔주기(2624)와 같은 문제

dp[w] = v 를 알아채는 것이 어려웠다.
같은 w에 대해, v가 가장큰 물건 조합1개만 트레킹하면 된다는점 캐치.

iter1: 동전1 썻을떄 가능한 w,v 들
iter2: 동전2 추가로 썻을떄 가능한 w,v들..
'''

# 무게 w, 가치 v
import sys

N,K = map(int, input().split())
wv = []
for _ in range(N):
    w,v = map(int, sys.stdin.readline().split())
    wv.append((w,v))

# wv.sort(reverse=True)

dp = [float("-inf")]*(K+1) # dp[w] = v
dp[0] = 0

for i in range(N):
    w,v = wv[i]

    # for j in range(len(dp)):
    #     if j-w < 0:
    #         continue
    #     dp[j] = max(dp[j], dp[j-w]+v)

    # dp =  x x x x x  x x x x x
    for j in range(len(dp)-1,-1,-1):
        if j - w >= 0 and dp[j-w] != -1:
            dp[j] = max(dp[j], dp[j-w]+v)
    
print(max(dp))
