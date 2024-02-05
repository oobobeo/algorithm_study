# 1238

from collections import defaultdict
from heapq import *
from math import inf

N,M,X = map(int, input().split())

pos_flow = defaultdict(list)
neg_flow = defaultdict(list)

for _ in range(M):
    s,e,t = map(int, input().split())
    pos_flow[s].append((e,t))
    neg_flow[e].append((s,t))

# dijkstra x 2
total_dists = []

h = [(0,X)]
dists = [inf]*(N+1)
dists[X] = 0
while h:
    d, cur = heappop(h)
    if d > dists[cur]: continue
    
    for nxt, cost in pos_flow[cur]:
        if dists[nxt] > dists[cur]+cost:
            dists[nxt] = dists[cur]+cost
            heappush(h, (dists[nxt], nxt))
total_dists.append(dists)


h = [(0,X)]
dists = [inf]*(N+1)
dists[X] = 0
while h:
    d, cur = heappop(h)
    if d > dists[cur]: continue
    
    for nxt, cost in neg_flow[cur]:
        if dists[nxt] > dists[cur]+cost:
            dists[nxt] = dists[cur]+cost
            heappush(h, (dists[nxt], nxt))
total_dists.append(dists)
# print(total_dists)
result = []
for i,x in enumerate(zip(*total_dists)):
    if i == 0: continue
    result.append((sum(x),i))
result.sort()
print(result[-1][0])
    
