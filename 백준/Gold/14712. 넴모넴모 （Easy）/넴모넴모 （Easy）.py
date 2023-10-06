N,M = map(int, input().split())

board = [[0]*(M+1) for _ in range(N+1)]

def nxt(x,y):
    if y < M:
        return (x,y+1)
    else:
        return (x+1,1)
# dfs, but (0,0) -> (0,1) -> (1,0) -> (1,1)
ans = 0
def dfs(x,y):
    global ans
    if x > N or y > M:
        ans += 1
        return   
    
    # print(board)
    
    next_coor = nxt(x,y)
    # print(*next_coor)
    # cur x
    dfs(*next_coor)
        
    # cur o
    if board[x-1][y-1] == 1 and board[x][y-1] == 1 and board[x-1][y] == 1:
        return
    else:
        board[x][y] = 1
        dfs(*next_coor)
        board[x][y] = 0
    
dfs(1,1)
print(ans)
