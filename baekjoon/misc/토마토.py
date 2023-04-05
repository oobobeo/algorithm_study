# 7576

import sys
from collections import deque

n, m = map(int, input().split())
board = []
visited = [[0]*n for _ in range(m)]
distance = [[0]*n for _ in range(m)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for _ in range(m):
    board.append(list(map(int, sys.stdin.readline().split())))

# BFS
queue = deque()
for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            visited[i][j] = 1
            queue.append([i,j])

while len(queue) > 0:
    curr = queue.popleft()
    curr_dist = distance[curr[0]][curr[1]]
    for dir in range(4):
        x = curr[0] + dx[dir]
        y = curr[1] + dy[dir]
        if x < 0 or x >= m or y < 0 or y >= n:
            continue
        if visited[x][y] or board[x][y] == -1:
            continue
        visited[x][y] = 1
        distance[x][y] = curr_dist + 1
        queue.append([x,y])

# check board
impossible_flag = 0
for i in range(m):
    for j in range(n):
        if board[i][j] == 0 and visited[i][j] == 0:
            impossible_flag = 1
            break
    if impossible_flag:
        break

# print result
all_distances = set()
for row in distance:
    all_distances = all_distances | set(row)
max_dist = 0
for i in all_distances:
    if i > max_dist:
        max_dist = i

if impossible_flag:
    print(-1)
else:
    print(max_dist)


