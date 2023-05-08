# 2225

'''
진정한 쉬운 dp
'''

N,K = map(int, input().split())
dp = [[0]*(N+1) for _ in range(K+1)]
dp[1] = [1]*(N+1)

for k in range(2,K+1):
    for i in range(N+1):
        dp[k][i] = sum(dp[k-1][:i+1])
# print(dp)
print(dp[K][N]%1000_000_000)
