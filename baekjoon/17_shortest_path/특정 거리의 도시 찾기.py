# 18352

import sys
from collections import defaultdict, deque


N,M,K,X = map(int, input().split())

nxt = defaultdict(list)
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    nxt[a].append(b)

# bfs
dists = [400000]*(N+1)
dists[X] = 0
q = deque([(X,0)])
while q:
    cur, d = q.popleft()
    if d > K:
        continue
    # if cur != X and dists[cur] <= d:
    #     continue
    
    for nei in nxt[cur]:
        if dists[nei] > d+1:
            q.append((nei, d+1))
            dists[nei] = d+1

ans = []
# print(dists)
for i,d in enumerate(dists):
    if d == K:
        ans.append(i)
if len(ans) != 0:
    for a in ans:
        print(a)
else:
    print(-1)
