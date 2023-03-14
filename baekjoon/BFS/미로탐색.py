# 2178

import sys
from collections import deque

n, m = map(int, input().split())
board = []
visited = [[0]*m for _ in range(n)]
distance = [[0]*m for _ in range(n)]
distance[0][0] = 1

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for _ in range(n):
    board.append( [int(i) for i in sys.stdin.readline().strip()] )
    
# BFS
done_flag = 0
queue = deque()
visited[0][0] = 1
queue.append([0,0])
while len(queue) > 0:
    curr = queue.popleft()
    curr_dist = distance[curr[0]][curr[1]]
    for dir in range(4):
        x = curr[0] + dx[dir]
        y = curr[1] + dy[dir]
        if x < 0 or x >= n or y < 0 or y >= m:
            continue
        if visited[x][y] or board[x][y] == 0:
            continue
        visited[x][y] = 1
        distance[x][y] = curr_dist + 1
        queue.append([x,y])
        if x == n-1 and y == m-1:
            done_flag = 1
            break
    if done_flag:
        break

print(distance[n-1][m-1])
