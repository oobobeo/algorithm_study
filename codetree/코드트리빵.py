from collections import deque

'''
num1: 1 min start
numN: N min start

per 1 min:
1. 가고 싶은 편의점 향해 1칸 (up, left, right, down)
2. 도착 -> halt
        [다른사람: 해당 편의점 못지나감]
3. if (t<=m):
        t번: 자신의 편의점과 closest basecamp에 들감. (같은거 여러개: 행,열이 가장 작은)
        [시간소요 x]
        [다른사람: 해당 basecamp 못지나감]
'''

N,M = map(int, input().split()) # NxN, num of pp = M
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
temp = []
for _ in range(M):
    temp.append(list(map(int, input().split())))
dest_coors = [(x-1,y-1) for x,y in temp]

    
basecamps = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            basecamps.append((i,j))
            
pp_coors = [(99999,99999)]*M
done = [0]*M


def neighbor(x,y):
    dir = [(-1,0), (0,-1), (0,1), (1,0)]
    temp = [(x+d1,y+d2) for d1,d2 in dir if x+d1 >= 0 and x+d1 < N and y+d2 >= 0 and y+d2 < N]
    nei = []
    for a,b in temp:
        if board[a][b] != -1:
            nei.append((a,b))
    return nei

def to_basecamp(pp_idx):
    global basecamps
    x,y = dest_coors[pp_idx]
    
    # bfs
    cands = []
    min_dist = 10000000
    q = deque([(x,y,0)])
    visited = [[0]*N for _ in range(N)]
    visited[x][y] = 1
    while q:
        x,y,d = q.popleft()
        if (x,y) in basecamps:
            # print('aa')
            # print(x,y,d)
            if d == min_dist:
                cands.append((x,y))
                continue
            if d < min_dist:
                cands = [(x,y)]
                min_dist = d
        for nei in neighbor(x,y):
            if not visited[nei[0]][nei[1]]:
                visited[nei[0]][nei[1]] = 1
                q.append((*nei, d+1))
    cands.sort()
    # print(cands)
    goto = cands[0]
    pp_coors[pp_idx] = goto
    
    idx = basecamps.index(goto)
    basecamps = basecamps[:idx]+basecamps[idx+1:]
    
    # print(pp_idx, goto, basecamps)
    return goto



def move(pp_idx):
    # print(pp_coors, pp_idx)
    x,y = pp_coors[pp_idx]
    a,b = dest_coors[pp_idx]
    
    visited = [(x,y)]
    dists = {str(x)+str(y): 0}
    global next_coor
    # print('a,b',a,b)
    def _dfs(x,y,d,hist):
        global next_coor
        # global next_coor
        # print('x,y',x,y,d,hist)
        # print('dists:', dists)
        if (x,y) == (a,b): # and (str(x)+str(y) not in dists or dists[str(x)+str(y)] > d):
            # print('HHHHHHHH')
            # print((str(x)+str(y)))
            # print(dists)
            # print((dists[str(x)+str(y)] > d))
            # print('d',d)
            # # next_coor = hist[0]
            # print(pp_idx,'coor',x,y,hist)
            next_coor = hist[0]
            return
        for x1,y1 in neighbor(x,y):
            key = str(x1)+str(y1)
            if (x1,y1) not in visited or (key in dists and dists[key] > d+1):
                visited.append((x1,y1))
                dists[key] = d+1
                hist.append((x1,y1))
                _dfs(x1,y1,d+1,hist)
                hist.pop()
    _dfs(x,y,0,[])
    
    # print()
    # print()
    # print('next_coor:', next_coor)
    # print()
    # print()
    
    pp_coors[pp_idx] = next_coor
    
    if next_coor == dest_coors[pp_idx]:
        done[pp_idx] = 1
        return next_coor
    else:
        return None
    
    
# B
# 0: 빈, 1: basecamp, -1: nopass

# time = 1
# pp = 0 ~ N-1

time = 1
nopass_coors = []
nopass_coors.append(to_basecamp(0))


for time in range(2,100000): # t >= 2
    # 1. move
    # 2. basecamp
    # 3. update board with nopass (basecamp/store)
    for i in range(time-1):
        if i < M and done[i] == 0:
            next_coor = move(i)
        if next_coor:
            nopass_coors.append(next_coor)
            
    for x,y in nopass_coors:
        board[x][y] = -1
        
    if time-1 < M:
        nopass_coors.append(to_basecamp(time-1))
    
    for x,y in nopass_coors:
        board[x][y] = -1
        
    # print()
    # print('t', time)
    # for l in board:
    #     print(l)
    # print('done', done)
    # print('pp_coors', pp_coors)
    
    if 0 not in done:
        break

print(time)



