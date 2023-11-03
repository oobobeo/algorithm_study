# NxN, M walls, K coolness
N,M,K = map(int, input().split())
board_info = [list(map(int, input().split())) for _ in range(N)]
wall_info = [list(map(int, input().split())) for _ in range(M)]

board = [[0]*N for _ in range(N)]
walls = [[[0]*4 for _ in range(N)] for _ in range(N)]
aircons = [] # (x,y,dir)
rooms = []

for i in range(N):
    for j in range(N):
        if board_info[i][j] == 1:
            rooms.append((i,j))
        elif board_info[i][j] >= 2:
            aircons.append((i,j,board_info[i][j]))
for w in wall_info:
    x,y,dir = w
    walls[x-1][y-1][dir^1] = 1
    if dir == 0 and x-2 >= 0:
        walls[x-2][y-1][3] = 1
    elif dir == 1 and y-2 >= 0:
        walls[x-1][y-2][2] = 1

###

def next(x,y,dir):
    #       l,u,r,d
    # dir = 2,3,4,5
    ret = []
    if dir == 3: # up
        if x-1 >= 0 and walls[x][y][1] == 0:
            ret.append((x-1,y))
        if x-1 >= 0 and y-1 >= 0 and walls[x][y-1][1] == 0 and walls[x][y-1][2] == 0:
            ret.append((x-1,y-1))
        if x-1 >= 0 and y+1 < N and walls[x][y+1][0] == 0 and walls[x][y+1][1] == 0:
            ret.append((x-1,y+1))
    elif dir == 5: # down
        if x+1 < N and walls[x][y][3] == 0:
            ret.append((x+1,y))
        if x+1 < N and y-1 >= 0 and walls[x][y-1][2] == 0 and walls[x][y-1][3] == 0:
            ret.append((x+1,y-1))
        if x+1 < N and y+1 < N and walls[x][y+1][0] == 0 and walls[x][y+1][3] == 0:
            ret.append((x+1,y+1))
            
    elif dir == 2: # left
        if y-1 >= 0 and walls[x][y][0] == 0:
            ret.append((x,y-1))
        if x-1 >= 0 and y-1 >= 0 and walls[x-1][y][0] == 0 and walls[x-1][y][3] == 0:
            ret.append((x-1,y-1))
        if x+1 < N and y-1 >= 0 and walls[x+1][y][0] == 0 and walls[x+1][y][1] == 0:
            ret.append((x+1,y-1))
    elif dir == 4: # right
        if y+1 < N and walls[x][y][2] == 0:
            ret.append((x,y+1))
        if x-1 >= 0 and y+1 < N and walls[x-1][y][2] == 0 and walls[x-1][y][3] == 0:
            ret.append((x-1,y+1))
        if x+1 < N and y+1 < N and walls[x+1][y][1] == 0 and walls[x+1][y][3] == 0:
            ret.append((x+1,y+1))
    return ret
        

def blow():
    temp_total = [[0]*N for _ in range(N)]
    for x,y,dir in aircons:
        temp = [[0]*N for _ in range(N)]
        if walls[x][y][dir-2] == 1:
            continue
        if dir == 2:
            y -= 1
        elif dir == 3:
            x -= 1
        elif dir == 4:
            y += 1
        elif dir == 5:
            x += 1
        if x >= 0 and x < N and y >= 0 and y < N: # first block condition
            temp[x][y] = 5
            curs = [(x,y)]
            for cool in range(4,0,-1):
                nexts = []
                for cur in curs:
                    nexts += next(*cur, dir)
                # print('x,y,dir,nexts', x,y,dir,nexts)
                for nn in list(set(nexts)):
                    temp[nn[0]][nn[1]] = cool
                curs = nexts
                
        for i in range(N):
            for j in range(N):
                temp_total[i][j] += temp[i][j]
    for i in range(N):
        for j in range(N):
            board[i][j] += temp_total[i][j]
    

def mix():
    temp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # left
            if j-1 >= 0 and walls[i][j][0] == 0:
                diff = abs(board[i][j] - board[i][j-1])//4
                if board[i][j] > board[i][j-1]:
                    temp[i][j] -= diff
                    temp[i][j-1] += diff
                else:
                    temp[i][j] += diff
                    temp[i][j-1] -= diff
                    
            # up
            if i-1 >= 0 and walls[i][j][1] == 0:
                diff = abs(board[i][j] - board[i-1][j])//4
                if board[i][j] > board[i-1][j]:
                    temp[i][j] -= diff
                    temp[i-1][j] += diff
                else:
                    temp[i][j] += diff
                    temp[i-1][j] -= diff
    for i in range(N):
        for j in range(N):
            board[i][j] += temp[i][j]
                    
def decrease():
    for i in range(N):
        for j in range(N):
            if i == 0 or j == 0 or i == N-1 or j == N-1:
                if board[i][j] >= 1:
                    board[i][j] -= 1

def check():
    for x,y in rooms:
        if board[x][y] < K:
            return False
    return True


for time in range(1,101):
    blow()
    mix()
    decrease()
    if check():
        print(time)
        exit(0)
    for l in board:
        print(*l)
    print('----',time,'----')
print(-1)



