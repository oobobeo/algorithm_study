# 4179

import sys
from collections import deque

n, m = map(int, input().split())
board = []
visited = [[0]*m for _ in range(n)]
distance = [[0]*m for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for _ in range(n):
    board.append(list(sys.stdin.readline().strip()))

# BFS
# init
J_coor = [-1, -1]
queue = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 'F':
            visited[i][j] = 'F'
            queue.append([i,j])
        elif board[i][j] == 'J':
            visited[i][j] = 'J'
            J_coor = [i,j]
queue.appendleft(J_coor)

# print(board)


# loop
total_distance = 0
success_flag = 0
while len(queue) > 0:
    curr = queue.popleft()
    curr_dist = distance[curr[0]][curr[1]]

    # print(curr)
    # for v in visited:
    #     print(v)

    # if curr is J
    if visited[curr[0]][curr[1]] == 'J':
        for dir in range(4):
            x = curr[0] + dx[dir]
            y = curr[1] + dy[dir]
            if x < 0 or x >= n or y < 0 or y >= m: # escaped!
                total_distance = curr_dist + 1
                success_flag = 1
                break
            if visited[x][y] == 'F' or visited[x][y] == 'J' or board[x][y] == '#':
                continue
            visited[x][y] = 'J'
            distance[x][y] = curr_dist + 1
            queue.append([x,y])
    # elif curr is F
    elif visited[curr[0]][curr[1]] == 'F':
        for dir in range(4):
            x = curr[0] + dx[dir]
            y = curr[1] + dy[dir]
            if x < 0 or x >= n or y < 0 or y >= m:
                continue
            if visited[x][y] == 'F' or board[x][y] == '#':
                continue
            if visited[x][y] == 'J':
                visited[x][y] = 'F'
                continue
            visited[x][y] = 'F'
            queue.append([x,y])
    if success_flag: break

# print result
if success_flag:
    print(total_distance)
else:
    print("IMPOSSIBLE")


