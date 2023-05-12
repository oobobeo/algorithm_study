# 2758

'''
아이디어 알면 구현은 쉬웠음 (1시간 정도 걸림)
'''

N,M = 11,2001

# dp init
dp = [[0]*(M+1) for _ in range(N+1)] # dp[max][num_of_lottery]
# dp[i][j] = dp[i-1][j-1] + dp[i][j//2]
for i in range(M+1):
    dp[1][i] = i
    
# dp
for i in range(2,N+1):
    for j in range(2**(i-1),M+1):
        dp[i][j] = dp[i-1][j//2] + dp[i][j-1]

T = int(input())
for _ in range(T):
    N,M = map(int, input().split())
    print(dp[N][M])
