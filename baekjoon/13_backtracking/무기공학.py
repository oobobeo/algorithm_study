# 18430

R,C = map(int, input().split())

arr = [[0]*(C+2)]
for _ in range(R):
    temp = []
    arr.append([0] + list(map(int, input().split())) + [0])
arr += [[0]*(C+2)]

used = [[0]*(C+2) for _ in range(R+2)]
mid = [[0]*(C+2) for _ in range(R+2)]


for i in range(R+2):
    for j in range(C+2):
        if i == 0 or j == 0 or i == R+1 or j == C+1:
            arr[i][j] = -1
            used[i][j] = -1
            
def nxt(x,y):
    if y <= C:
        return (x,y+1)
    else:
        return (x+1, 1)

dir = [(-1,0),(0,1),(1,0),(0,-1),(-1,0)]
def possible_coors(x,y):
    ret = []
    for i in range(4):
        x1,y1 = x+dir[i][0],y+dir[i][1]
        x2,y2 = x+dir[i+1][0],y+dir[i+1][1]
        if used[x][y] == 0 and used[x1][y1] == 0 and used[x2][y2] == 0:
            ret.append([[x,y],[x1,y1],[x2,y2]])
    return ret
   
"""
(0,0) -> (0,1) -> (1,0) -> .. dfs
중심잡고 먹을지 안먹을지
    1. 안먹고 nxt dfs
    2. 먹고 nxt dfs
""" 
max_score = 0
def dfs(x,y):
    global max_score
    next = nxt(x,y)
    
    if next[0] >= R+1:
        score = 0
        for i in range(R):
            for j in range(C):
                if used[i+1][j+1] == 1:
                    score += arr[i+1][j+1]
                if mid[i+1][j+1] == 1:
                    score += arr[i+1][j+1]
        max_score = max(max_score, score)
        return
    
    if used[x][y] == 1:
        dfs(*next)
        return
        
    # 1
    dfs(*next)
    # 2
    if possible_coors(x,y):
        for c3 in possible_coors(x,y):
            mid[x][y] = 1
            for i in range(3):
                used[c3[i][0]][c3[i][1]] = 1
            dfs(*next)
            mid[x][y] = 0
            for i in range(3):
                used[c3[i][0]][c3[i][1]] = 0
        
dfs(1,1)
print(max_score)