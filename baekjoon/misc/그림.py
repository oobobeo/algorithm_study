# 1926

import sys
from collections import deque

n, m = map(int, input().split())
board = []
visited = [[0]*m for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

total_num = 0
total_sizes = []
for i in range(n):
    for j in range(m):
        # select starting node.
        if board[i][j] == 0 or visited[i][j]:
            continue
        # metadata
        total_num += 1
        size = 0
        # BFS
        queue = deque()
        visited[i][j] = 1
        queue.append([i,j])
        while len(queue) > 0:
            size += 1
            curr = queue.popleft()
            for dir in range(4):
                x = curr[0] + dx[dir]
                y = curr[1] + dy[dir]
                if x < 0 or x >= n or y < 0 or y >= m:
                    continue
                if visited[x][y] or board[x][y] == 0:
                    continue
                visited[x][y] = 1
                queue.append([x,y])
        total_sizes.append(size)

biggest_size = 0
total_sizes = sorted(total_sizes)
if total_sizes:
    biggest_size = total_sizes[-1]
print(total_num, biggest_size, sep='\n')

