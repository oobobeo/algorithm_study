# 22868


'''
재귀 dfs 2번 완전탐색은 timeout 난다.

idea) 
1. conn[x]를 사전순 배열.
2. bfs (bfs는 queue 밖에 없다.)
3. end 가 가장 먼저 도달하는 route가 최단거리 + 사전순 가장 빠르다..
맞나?

맞다.


'''

from collections import defaultdict, deque
import sys

sys.setrecursionlimit(10**6)

con = defaultdict(list)
N,M = map(int, input().split())
for _ in range(M):
    a,b = map(int, input().split())
    con[a].append(b)
    con[b].append(a)
S,E = map(int, input().split())

# S->E->S
# S->E, E->S 다른경로
# 짧은 경로 중, 사전순 빠른거.


# 1--2--4
# | /  /
# 3---

def dfs(st, en, visited):
    # init
    q = deque([[st]]) # [(hist), ..]
    visited[st] = 1
    
    # main
    while q:
        cur_hist = q.popleft()
        cur = cur_hist[0]
        if cur == en:
            return cur_hist
        for n in sorted(con[cur]):
            if visited[n] == 0:
                visited[n] = 1
                q.append(([n] + cur_hist))
        

# S -> E
visited = [0]*(N+1)
route1 = dfs(S, E, visited) # E ~ S

# E -> S
visited = [0]*(N+1)
for n in route1[:-1]: # exclude S
    visited[n] = 1
route2 = dfs(E, S, visited)

print(len(route1) + len(route2) - 2)





# min_len = 20000
# cands1 = []
# visited = [0]*(N+1)
# visited[S] = 1
# def dfs1(cur, hist, visited):
#     global min_len
#     if len(hist) > min_len:
#         return
#     if cur == E:
#         min_len = min(min_len, len(hist))
#         cands1.append(hist[:])
#         return
#     for n in sorted(con[cur]):
#         if visited[n] == 0:
#             visited[n] = 1
#             dfs1(n, hist+[n], visited)
#             visited[n] = 0

# dfs1(S, [S], visited)
# # print(cands1)
# # print(visited)

# cands1 = sorted([r for r in cands1 if len(r) == min_len])
# route1 = cands1[0]


# # E -> S

# min_len = 20000
# cands2 = []
# visited = [0]*(N+1)
# for n in route1:
#     visited[n] = 1
# visited[S] = 0

# def dfs2(cur, hist, visited):
#     global min_len
#     if len(hist) > min_len:
#         return
#     if cur == S:
#         min_len = min(min_len, len(hist))
#         cands2.append(hist[:])
#         return
#     for n in con[cur]:
#         if visited[n] == 0:
#             visited[n] = 1
#             dfs2(n, hist+[n], visited)
#             visited[n] = 0

# cands2 = sorted([r for r in cands2 if len(r) == min_len])
# route2 = cands1[0]

# print(len(route1) + len(route2) - 2)
