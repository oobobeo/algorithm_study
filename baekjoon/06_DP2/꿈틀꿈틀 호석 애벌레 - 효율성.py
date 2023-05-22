# 20181


'''
복잡하게 dp[N][3] 으로 경우수를 나눠서 풀었는데 작동하지 않고, 어디서 잘못됐는지 찾기도 어렵다. (70줄)


dp + 2_pointer 로 푼 풀이를 보고 따라 풀었다.
dp[r] = r까지 봤을때, 최대 포만감 (r안먹는 경우도 포함)
<sol>
cur_sum = sum(arr[l:r+1]) 이 K 이상인 경우들에 대해( l~r 사이 먹이들로 >K 만들기 가능한 경우만 고려 )
    dp[r] = max(dp[r], dp[l-1] + (cur_sum - K)) # l-1까지 최대 포만감 + l~r다 먹어서 포만감.
    l~r을 먹었을 때
--

<explanation>
dp[r]까지 먹었을 때 포만감을 얻는 l 에 대한 dp이다.
    r에대해 l은 여러개일 수 있다.
r이 연속 하지 않을 수 있다.
포만감을 얻어야지만 전체포만감에 변화가 있으므로 이렇게 푼다.

<2_pointer validity>
r이 커졌을때, l은 항상 커지거나 같으므로 valid
dp[r]을 찾을떄, (l~r-1) 구간이 >K


edge1) dp[++r] 했을때 포만감 못얻는경우 (dp[r] = dp[r-1])
edge2) dp[0] 일때 포만감 얻는 경우
'''

import sys

N, K = map(int, input().split())
arr = [0] + list(map(int, sys.stdin.readline().split()))

# init
dp = [0]*(N+1)
l = r = 0
cur_sum = arr[0]
if cur_sum >= K:
    dp[0] = cur_sum - K

# dp
# dp[r] = dp[l-1] + cur_sum(l ~ r) - K
while r <= N-1: # for r:1~N-1
    r += 1
    cur_sum += arr[r]
    dp[r] = dp[r-1]
    while cur_sum >= K:
        dp[r] = max(dp[r], dp[l-1] + cur_sum - K)
        cur_sum -= arr[l]
        l += 1



# print(dp)
print(dp[N])









'''
경우수 나눠서 한 dp. 작동하지 않는다..
'''
# dp = [[(-1, -1)]*3 for _ in range(N)]  # dp[N][3] = (acc_sum, cur_sum)
# if arr[0] >= K:
#     dp[0][0] = (0, 0)
#     dp[0][1] = (arr[0]-K, 0)
#     dp[0][2] = (0, 0)
# if arr[0] <= K:
#     dp[0][0] = (0, arr[0])
#     dp[0][1] = (0, 0)
#     dp[0][2] = (0, 0)

# # dp[i][0] = i먹, 오바x
# # dp[i][1] = i먹, 오바o
# # dp[i][2] = i안먹

# # check validity of dp[i][j]
# def v(i, j):
#     if dp[i][j][0] == -1:
#         return False
#     else:
#         return True


# for i in range(1, N):
#     # i먹, 오바x
#     # 1. i-1먹o (오바x) -> i먹 (오바x)
#     # 2. i-1먹o (오바o) -> i먹 (오바x)
#     # 3. i-1먹x        -> i먹 (오바x)
#     cand = []
#     if v(i-1, 0) and dp[i-1][0][1] + arr[i] < K:
#         cand.append((dp[i-1][0][0], dp[i-1][0][1]+arr[i]))
#     if arr[i] < K:
#         if v(i-1, 1):
#             cand.append((dp[i-1][1][0], arr[i]))
#         if v(i-1, 2):
#             cand.append((dp[i-1][2][0], arr[i]))
#     if cand:
#         dp[i][0] = sorted(cand)[-1]
#     else:
#         dp[i][0] = (-1, -1)

#     # i먹, 오바o
#     # 1. i-1먹o (오바x) -> i먹 (오바)
#     # 2. i-1먹o (오바o) -> i먹 (오바)
#     # 3. i-1먹x        -> i먹 (오바)
#     cand = []
#     if v(i-1, 0) and dp[i-1][0][1] + arr[i] >= K:
#         cand.append((dp[i-1][0][0]+dp[i-1][0][1]+arr[i]-K, 0))
#     if arr[i] >= K:
#         if v(i-1, 1):
#             cand.append((dp[i-1][1][0]+arr[i]-K, 0))
#         if v(i-1, 2):
#             cand.append((dp[i-1][2][0]+arr[i]-K, 0))
#     if cand:
#         dp[i][1] = sorted(cand)[-1]
#     else:
#         dp[i][1] = (-1, -1)

#     # i-1먹 (오바o) -> i먹x
#     # or i-1먹x    -> i먹x
#     cand = []
#     if v(i-1, 1):
#         cand.append(dp[i-1][1])
#     if v(i-1, 2):
#         cand.append(dp[i-1][2])
#     if cand:
#         dp[i][2] = sorted(cand)[-1]
#     else:
#         dp[i][2] = (-1, -1)


# for i,l in enumerate(dp):
#     print(arr[i],l)

# print(sorted(dp[-1])[-1][0])
