# 17485

'''
복잡하구만
'''

import sys

N,M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

inf = float("inf")
# 각 block당, 현재 block에 들어온 방향 3가자
dp = [[[arr[0][i]]*3 for i in range(M)]] + [[[inf]*3 for __ in range(M)] for _ in range(N-1)]
# for i in range(len(dp)):
#     print(dp[i])
# print('------------')

for i in range(1,N):
    for j in range(M):
        a,b,c = j-1,j,j+1
        if a < 0:
            dp[i][j][1] = dp[i-1][b][2] + arr[i][j]
            dp[i][j][2] = min(dp[i-1][c][0], dp[i-1][c][1]) + arr[i][j]
            # dp[i][j][0] = inf
            continue
        elif c > M-1:
            dp[i][j][1] = dp[i-1][b][0] + arr[i][j]
            dp[i][j][0] = min(dp[i-1][a][2], dp[i-1][a][1]) + arr[i][j]
            # dp[i][j][2] = inf
            continue
        else:
            # print(a,c)
            dp[i][j][0] = min(dp[i-1][a][2], dp[i-1][a][1]) + arr[i][j]
            dp[i][j][1] = min(dp[i-1][b][0], dp[i-1][b][2]) + arr[i][j]
            dp[i][j][2] = min(dp[i-1][c][0], dp[i-1][c][1]) + arr[i][j]

# for i in range(len(dp)):
#     print(dp[i])
ans = []
for i in range(len(dp[N-1])):
    ans.append(min(dp[N-1][i]))
print(min(ans))





