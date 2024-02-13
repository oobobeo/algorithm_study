# 1766

import sys
from collections import defaultdict
from heapq import *

N,M = map(int, input().split())

indeg = [0]*(N+1)
nxts  = defaultdict(list)
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    nxts[a].append(b)
    indeg[b] += 1

ans = []
h = []
for i in range(len(indeg)):
    if i == 0: continue
    if indeg[i] == 0:
        heappush(h, i)
        
while h:
    cur = heappop(h)
    ans.append(cur)
    
    for nxt in nxts[cur]:
        indeg[nxt] -= 1
        if indeg[nxt] == 0:
            heappush(h, nxt)

print(*ans)
