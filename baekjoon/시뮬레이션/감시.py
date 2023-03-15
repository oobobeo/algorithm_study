# 15683


import itertools
import sys
import copy

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(sys.stdin.readline().split())


# detect camera & wall
# right: 1, down: 2, left:4, up:8
# camera1: 1,2,4,8
# camera2: 5,10
# camera3: 3,6,9,12
# camera4: 7,11,13,14
# camera5: 15
# orientation = [[0]*m for _ in range(n)]
cameras = [] # (x,y,orientation)
for i in range(n):
    for j in range(m):
        if board[i][j] == '1' or board[i][j] == '2' or board[i][j] == '3' or board[i][j] == '4' or board[i][j] == '5':
            cameras.append([i,j,board[i][j]])
        elif board[i][j] == '6':
            pass


# [orientation of each camera]
orientaions = []
for _,_,i in cameras:
    if i == '1':
        orientaions.append([1,2,4,8])
    elif i == '2':
        orientaions.append([5,10])
    elif i == '3':
        orientaions.append([3,6,9,12])
    elif i == '4':
        orientaions.append([7,11,13,14])
    elif i == '5':
        orientaions.append([15])
orientaions = list(itertools.product(*orientaions))

# print(orientaions)

# ori to dir
# right:(0,1), down:(1,0), left:(0,-1), up:(-1,0)
def ori2dir(num):
    result = []
    if num >> 3:
        result.append([-1,0])
    if (num % 8) >> 2:
        result.append([0,-1])
    if (num % 4) >> 1:
        result.append([1,0])
    if num % 2 == 1:
        result.append([0,1])
    return result

# update map by checking camera sights
# map: deepcopied board
# x,y: camera coor
# dirs: camera dirs
# sighted = ' '
def update(map, x, y, dirs):
    # print(map, x, y, dirs)
    for dir in dirs:
        nx,ny = x,y
        while True:
            nx += dir[0]
            ny += dir[1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: break
            if map[nx][ny] == '6': break
            if map[nx][ny] in ['1','2','3','4','5']: continue
            # print(nx,ny)
            map[nx][ny] = ' '



# for oris in orientaions:
#     print(oris)


# calculate blind spots
blind_spots = n*m
for oris in orientaions:
    # print(oris)
    map = copy.deepcopy(board)

    # update map
    all_dirs = [ori2dir(ori) for ori in oris]
    # print(all_dirs)
    for i in range(len(cameras)):
        x,y,_ = cameras[i]
        dirs = all_dirs[i] # [[-1,0],[1,0]]
        update(map, x, y, dirs)
    
    # check blind spots
    temp = 0
    for i in range(n):
        for j in range(m):
            if map[i][j] == '0':
                temp += 1
    blind_spots = min(blind_spots, temp)

print(blind_spots)





