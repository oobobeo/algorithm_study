# 2228

'''
풀다가 모르겠어서 답 찾아봄.
dp[m][i] = 구간m개, arr[0:i+1] 의 max 값.
dp[m][i] = 
    case1) i 사용x -> dp[m][i-1]
    case2) i 사용o -> [dp[m-1][k] + sum(arr[k+1:i+1])]: [k = 2m-2 ~ i] 중 max 값.
                                                        dp[m-1][k] 가 실제로 m-1개의 구간을 갖고 있어야한다.
edge1) m=1 일 떄, (case2) 계산시 `k in range(m*2-3,i)` 해주면 arr[0]이 sum(arr[k+1:i+1] 에서 빠지게됨.

어렵다!
'''

N,M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

dp = [[0]*N for _ in range(M+1)] # dp[m][i]

for m in range(1,M+1):
    # minimun possible length = m*2-1, idx = m*2-2
    temp = 0
    for odd in range(0,m*2-1,2):
        # print(m, odd, 'hhhh')
        temp += arr[odd]
    dp[m][m*2-2] = temp

    for i in range(m*2-1,N):
        # case1) # don't use arr[i]
        candidates = [dp[m][i-1]]

        # case2) use arr[i]
        # [0:k-1], [k+1:i+1]
        if m == 1:
            for k in range(i+1):
                candidates.append(sum(arr[k:i+1]))
        elif m >= 1:
            for k in range(m*2-3,i):
                if k-1 >= 0:
                    candidates.append(dp[m-1][k-1] + sum(arr[k+1:i+1]))
                else:
                    candidates.append(sum(arr[k+1:i+1]))

                
            # print('m k:',m,k,candidates)
        dp[m][i] = max(candidates)
        # if m == 2:
        #     print(m,i,candidates)

# for l in dp:
#     print(l)
print(dp[M][N-1])










'''
dp[m][i][j] = partition=m개, [i~j]구간의 max. 를 이용한 풀이. 복잡하고 틀렸다.
'''
# # [N-1 | 1] or [1 | N-1] -> [ N ]
# dp = [[[0]*N for _ in range(N)] for _ in range(M+1)]
# # dp[partition_num][i][j] = i~j largest sum



# # init
# for i in range(N):
#     for j in range(N):
#         dp[0][i][j] = sum(arr[i:j+1])
# for i in range(N):
#     dp[1][i][i] = arr[i]

# # O(N^4), N=100
# for m in range(1,M+1):
#     # dp
#     for a in range(0,N):
#         for b in range(N-a):
#             i,j = b,a+b
#             # edge1) no possible way to partition
#             if j-i+1 < m*2:
#                 dp[m][i][j] = 0
#             else:
#                 # [i ~ k-1|k|k+1 ~ j]
#                 # 2 cases)
#                 #   1. leftside: dp[1], rightside: dp[m-1]
#                 #   2. vice-versa
#                 temp = 0
#                 for k in range(i,j+1):
#                     # case1
#                     if k-i >= 1 and j+1-k >= 2*(m-1):
#                         temp = max(temp, dp[1][i][k-1] + dp[m-1][i][k-1])
#                     # case2
#                     if k-i > 2*(m-1) and j+1-k >= 1:
#                         temp = max(temp, dp[m-1][i][k-1] + dp[1][i][k-1])
#                 dp[m][i][j] = temp

# for l in dp:
#     print(l)
# print(dp[M][0][N-1])

# [i~j] 일때 옆에 뺴는거 전혀 고려안됨
# 걍 방향이 틀린거 같음


# 0
# 00
# 0x0
# 0x00
# 0x0x0
# 0x0x00
