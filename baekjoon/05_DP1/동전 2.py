# 2294

'''
동전바꿔주기(2624)랑 비슷한 문제

푸는데 엄청 오래 걸리다가 답보고 품..
dp[i] = min(dp[i],dp[i-offset*c]+offset) <- 이 부분이 모든 가능한 offset에 대해서 해줘야 되는줄 앎.

coin 1개에 대해 dp를 dp[0]->dp[K] 까지 업데이트를 하는데
i까지 업데이트 했을때, dp[0~i]는 optimal이다. <- 이걸 놓침
따라서 dp[m] = min(dp[i], dp[i-offset*1], dp[i-offset*2], ..) 해주지 않아도 된다. <- O(N*K^2)


'''

N,K = map(int, input().split())

coin = []
for _ in range(N):
    coin.append(int(input()))

coin.sort()

# init dp
dp = [1000000]*(K+1) # dp[cost] = # of coins used
dp[0] = 0
for i in range(N):
    if coin[i] > K:
        break
    dp[coin[i]] = 1

# dp
while coin:
    c = coin.pop()
    for i in range(c,K+1): # target = i
        offset = 1
        dp[i] = min(dp[i],dp[i-offset*c]+offset)
if dp[K] != 1000000:
    print(dp[K])
else:
    print(-1)

# 0 0 1 0 0 2 0 0 3
