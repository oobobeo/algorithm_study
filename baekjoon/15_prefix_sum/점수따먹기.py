# 1749

'''
왼쪽, 위쪽에 0-padding 해서 계산 간단하게 하고 edgecase 없애기

'''


N,M = map(int, input().split())
board = [[0]*(M+1)]
for _ in range(N):
    board.append([0]+list(map(int, input().split())))

arr = [[0]*(M+1) for _ in range(N+1)]
for i in range(N+1):
    for j in range(M+1):
        if i == 0 or j == 0:
            arr[i][j] = 0
        else:
            arr[i][j] = arr[i-1][j]+arr[i][j-1]-arr[i-1][j-1]+board[i][j]
        
ans = -1000000
for x1 in range(N):
    for x2 in range(x1+1,N+1):
        for y1 in range(M):
            for y2 in range(y1+1,M+1):
                ans = max(ans, arr[x2][y2]-arr[x1][y2]-arr[x2][y1]+arr[x1][y1])

for x in range(1,N+1):
    for y in range(1,M+1):
        ans = max(ans, arr[x][y])

print(ans)

print(arr)









