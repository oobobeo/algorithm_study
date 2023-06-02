# 17836

'''
recursive DFS로 풀음 -> time out
bfs로 품. -> 틀림
edge case들을 고려 안하고 풀면 이렇게 된다...
edge1) 칼안줍고 그냥 가기..

수업들으면서 풀면 확실히 집중도가 떨어지는거 같다.
'''

from collections import deque
from functools import lru_cache

N,M,T = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
    
gram_coor = ()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            gram_coor = (i,j)

@lru_cache(maxsize=10000)
def neighbor(coor):
    x,y = coor
    result = []
    if x-1 >= 0 and arr[x-1][y] in [0,2]:
        result.append((x-1,y))
    if y-1 >= 0 and arr[x][y-1] in [0,2]:
        result.append((x,y-1))
    if x+1 <= N-1 and arr[x+1][y] in [0,2]:
        result.append((x+1,y))
    if y+1 <= M-1 and arr[x][y+1] in [0,2]:
        result.append((x,y+1))
    return result


# 1. 그냥 공주로
# 2. 그람 -> 공주
visited = [[0]*M for _ in range(N)]
visited[0][0] = 1
# cand = []
# def dfs(coor, visited, time):
#     if coor == gram_coor:
#         cand.append(time + N-1-coor[0] + M-1-coor[1])
#         return
#     if coor == (N-1,M-1):
#         cand.append(time)
#     for n in neighbor(coor):
#         if visited[n[0]][n[1]] == 0:
#             visited[n[0]][n[1]] = 1
#             dfs(n, visited, time+1)
#             visited[n[0]][n[1]] = 0
            
cand = []
def bfs(coor, visited, time):
    global cand
    q = deque()
    q.append((0,0,0)) # (x,y,time)
    while q:
        x,y,time = q.popleft()
        coor = (x,y)
        if coor == (N-1,M-1):
            cand.append(time)
            return
        if coor == gram_coor:
            cand.append(time + N-1-coor[0] + M-1-coor[1])
        
        for n in neighbor((x,y)):
            if visited[n[0]][n[1]] == 0:
                visited[n[0]][n[1]] = 1
                q.append((n[0],n[1],time+1))
    
# dfs((0,0), visited, 0)
bfs((0,0), visited, 0)

if cand and min(cand) <= T:
    print(min(cand))
else:
    print("Fail")



