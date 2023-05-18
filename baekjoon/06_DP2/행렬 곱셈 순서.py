# 11049

'''
dp[i][j] = [i:j+1] 구간 min.
길이가 짧은 구간부터 구해나간다.
'''

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

inf = float("inf")
dp = [[inf]*N for _ in range(N)]

# [i:k+1] + [k+1:j+1]
def cal(i,j,k):
    len1 = k-i+1
    len2 = j-k
    if len1 == 1 and len2 == 1:
        return arr[i][0] * arr[i][1] * arr[j][1]
    if len1 == 1:
        return arr[i][0] * arr[i][1] * arr[j][1] + dp[k+1][j]
    if len2 == 1:
        return dp[i][k] + arr[j][0] * arr[j][1] * arr[i][0]
    return dp[i][k] + dp[k+1][j] + arr[i][0] * arr[k][1] * arr[j][1]



for a in range(1,N):
    for b in range(N-a):
        i,j = b,a+b
        cand = []
        for k in range(i,j): 
            cand.append(cal(i,j,k))
        dp[i][j] = min(cand)

# for l in dp:
#     print(l)

print(dp[0][N-1])





