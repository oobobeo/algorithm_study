# 20542

'''
'편집거리 알고리즘' 을 사용한 문제다..
모르겠어서 찾아봄.
[insert,delete,replace] 로 arr1->arr2 만드는 최소 수행횟수
dp[i][j] <- min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) 을 이용해 update
'''

# i -> i,j,l
# v -> v,w

import sys

N,M = map(int, input().split())
arr1 = list(input().strip())
arr2 = list(input().strip())

# N < M guaranteed
dp = [[0]*(M+1) for _ in range(N+1)]
for i in range(N+1):
    dp[i][0] = i
for j in range(M+1):
    dp[0][j] = j

for i in range(1,N+1):
    for j in range(1,M+1):
        if arr1[i-1] == arr2[j-1]\
            or (arr1[i-1] == 'i' and arr2[j-1] in ['i','j','l'])\
            or (arr1[i-1] == 'v' and arr2[j-1] in ['v', 'w']):
            dp[i][j] = max(min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]), abs(j-i))
        else:
            dp[i][j] = max(min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1, abs(j-i))

print(dp[N][M])
