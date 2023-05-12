# 1915

'''
아이디어 잡으면 쉽게 풀림
'''

import sys

N,M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip())))

# dp init
dp = [[0]*M for _ in range(N)] # (i,j) -> biggest square w/ current indices as the right-bottom vertex
for i in range(M):
    dp[0][i] = arr[0][i]
for j in range(N):
    dp[j][0] = arr[j][0]

# dp
result_candidates = [max(arr[0])]
for i in range(1,N):
    for j in range(1,M):
        if arr[i][j]:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    result_candidates.append(max(dp[i]))
print(max(result_candidates)**2)
