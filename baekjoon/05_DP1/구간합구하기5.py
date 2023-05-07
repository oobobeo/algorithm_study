# 11660

'''
agg_mat 구하고 이거 중심으로 ans계산해줌
'''

import sys

N,M = map(int, input().split())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

agg_mat = [[0]*N for _ in range(N)] # [i,j] = sum up to [i,j]
for i in range(N):
    for j in range(N):
        if i > 0 and j > 0:
            agg_mat[i][j] = agg_mat[i][j-1] + agg_mat[i-1][j] - agg_mat[i-1][j-1] + mat[i][j]
        elif i == 0 and j > 0:
            agg_mat[0][j] = agg_mat[0][j-1] + mat[0][j]
        elif i > 0 and j == 0:
            agg_mat[i][0] = agg_mat[i-1][0] + mat[i][0]
        else: # i == 0 and j == 0
            agg_mat[0][0] = mat[0][0]

# print(mat)
# print(agg_mat)

for _ in range(M):
    i,j,x2,y2 = map(int, sys.stdin.readline().split())
    i -= 1
    j -= 1
    x2 -= 1
    y2 -= 1

    if i > 0 and j > 0:
        ans = agg_mat[x2][y2] - agg_mat[x2][j-1] - agg_mat[i-1][y2] + agg_mat[i-1][j-1]
    elif i == 0 and j > 0:
        ans = agg_mat[x2][y2] - agg_mat[x2][j-1]
    elif i > 0 and j == 0:
        ans = agg_mat[x2][y2] - agg_mat[i-1][y2]
    else: # i == 0 and j == 0
        ans = agg_mat[x2][y2]
    print(ans)


