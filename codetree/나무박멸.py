import sys

N,M,K,C = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

# 0: 빈칸, 1~100: 나무, -1: 벽, -2~(-2-M): 제초제

# 
def neighbors(x,y):
    dir = [(-1,0),(1,0),(0,-1),(0,1)]
    cands = [(x+dir[i][0],y+dir[i][1]) for i in range(4) if x+dir[i][0] >= 0 and x+dir[i][0] < N and y+dir[i][1] >= 0 and y+dir[i][1] < N]
    return cands

# 제초제가 닿는 모든 칸
def diagonals(x,y):
    if arr[x][y] in [0,-1] or arr[x][y] <= -2:
        return [(x,y)]
    else:
        ret = [(x,y)]
        for d in [(-1,-1),(1,1),(1,-1),(-1,1)]:
            a,b = x,y
            for _ in range(K):
                a += d[0]
                b += d[1]
                if a >= 0 and a < N and b >= 0 and b < N:
                    if arr[a][b] >= 1: # tree
                        ret.append((a,b))
                    elif arr[a][b] == 0 or arr[a][b] <= -2: # empty space | 제초제
                        ret.append((a,b))
                        break
                    else: # wall
                        break
        return ret

def grow():
    growth = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0: # tree
                neighbor_tree_count = 0
                for nn in neighbors(i,j):
                    if arr[nn[0]][nn[1]] >= 1:
                        neighbor_tree_count += 1
                growth[i][j] += neighbor_tree_count
    # apply growth
    for i in range(N):
        for j in range(N):
            arr[i][j] += growth[i][j]    
            
    # print('growth')
    # for l in growth:
    #     print(*l)
    # print()

def reproduce():
    childs = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0: # tree
                empty_space = []
                for nn in neighbors(i,j):
                    if arr[nn[0]][nn[1]] == 0:
                        empty_space.append(nn)
                for e in empty_space:
                    childs[e[0]][e[1]] += (arr[i][j]//len(empty_space))
    print()
    print('childs')
    for l in childs:
        print(*l, sep='\t')
    # apply childs
    for i in range(N):
        for j in range(N):
            arr[i][j] += childs[i][j]    

kill_count = 0
def kill():
    global kill_count
    max_kills = -1 # 커져야지만(초과) 바뀜
    center = None
    for i in range(N):
        for j in range(N):
            diags = diagonals(i,j)
            if len(diags) == 0:
                continue
            temp = 0
            for dd in diags:
                if arr[dd[0]][dd[1]] >= 1:
                    temp += arr[dd[0]][dd[1]]
            if temp > max_kills:
                center = (i,j)
                max_kills = temp
    # apply
    kill_count += max_kills
    for dd in diagonals(*center):
        i,j = dd
        if arr[i][j] != -1:
            arr[i][j] = -C-2
            
# 제초제 update
def update_board():
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= -3:
                arr[i][j] += 1
            elif arr[i][j] == -2:
                arr[i][j] = 0
       
for _ in range(M):
    grow()
    reproduce()
    
    print()
    print(_, 'b4 kill')
    for l in arr:
        print(*l, sep='\t')
    print()
    
    kill()
    update_board()
    
    print(_, 'a4 kill')
    for l in arr:
        print(*l, sep='\t')
    print()
    
    print()
print(kill_count)
