# 16973

'''
오래 걸리고 문제가 많았다.
1. time out
    N,M = 1000의 직사각형이고 
    그 안에 agent의 크기가 자유이다.
    collsion detection(possible()) 이 (i,j)마다 agent 의 모든 점에 대해 다 확인해 줬는데
    이러면 O(N^4)이 되서 timeout이 난다..
    <sol>
    p[][] 만드는 과정을 O(N^2 + N)으로 하고, p[][]을 통해 O(1)로 (i,j)가 possible한지 알수있게 했다.
    전체 time complexity: O(N^2)
    
2. memory exceed
    BFS를 이용해 완전탐색을 했는데 memory exceed됐다.
    자료구조들은 [N]x[N] 해봤자 4MB여서 찾는데 오래걸렸다.
    <sol>
    문제는 q였다.
    q에 cur->neighbor 들을 넣어줄 떄, visited[][] 를 체크해주고 넘겨줘야된다..
    아니면 q.pop()했을 때 visited[][]확인 해주던가.
    barkingdog 형님의 말을 까먹지 말자!
'''


from collections import deque
import sys

N,M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
H,W,Sx,Sy,Fx,Fy = map(int, input().split())
Sx,Sy,Fx,Fy = Sx-1,Sy-1,Fx-1,Fy-1


# left_corner = (i,j)
# check if current coor is possible.
def possible(i,j):
    if i+H-1 > N-1: return False
    if j+W-1 > M-1: return False
    if i < 0: return False
    if j < 0: return False
    return p[i][j]

p = [[0]*M for _ in range(N)]
col_v = [[0]*M for _ in range(N)] # (i,j),(i+1,j),.. H만큼 더한 value
for i in range(N-H+1):
    for j in range(M):
        temp = 0
        for a in range(H):
            temp += arr[i+a][j]
        col_v[i][j] = temp

for i in range(N-H+1):
    cur = sum(col_v[i][:W])
    p[i][0] = (cur == 0)
    for j in range(1,M-W+1):
        cur = cur - col_v[i][j-1] + col_v[i][j+W-1]
        p[i][j] = (cur == 0)


# full search

# DFS init
visited = [[0]*M for _ in range(N)] # visited[i][j] = 0|1
visited[Sx][Sy] = 1
q = deque()
q.append((Sx,Sy,0))
d = [(-1,0),(1,0),(0,1),(0,-1)]
cands = []
while q:
    x,y,dist = q.popleft()
    ## 이 부분없으면 visit 된 부분에서 다시 탐색함.
    if visited[x][y]:
        continue
    ## ----------------------------------
    visited[x][y] = 1
    if x == Fx and y == Fy:
        cands.append(dist)
        continue
    
    neighbors = [(x+dd[0],y+dd[1]) for dd in d\
                  if possible(x+dd[0],y+dd[1])\
                #   if possible(x,y,dd[0],dd[1])\
                    and not visited[x+dd[0]][y+dd[1]]]
    for n in neighbors:
        q.append((*n,dist+1))

if cands:
    print(min(cands))
else:
    print(-1)
# print(cands)
