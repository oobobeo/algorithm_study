# 11404









MAX = 10000000

import sys
def input():
    return sys.stdin.readline().strip()

N = int(input())
M = int(input())

distance = [[MAX]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int, input().split())
    distance[a][b] = min(c, distance[a][b])
for i in range(1,N+1):
    distance[i][i] = 0

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])

for row in range(1,N+1):
    print(' '.join([str(i) if i < MAX else '0' for i in distance[row][1:]]))






