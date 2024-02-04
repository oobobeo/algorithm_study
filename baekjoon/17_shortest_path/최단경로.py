# 1753

'''
dijkstra 다시 숙지
'''

import sys
from collections import defaultdict
from heapq import *

INF = 300000

V,E = map(int, input().split())
K = int(input())

nxts = defaultdict(set)
weight = defaultdict(int)
for _ in range(E):
    u,v,w = map(int, sys.stdin.readline().split())
    nxts[u].add(v)
    key = (u,v)
    if weight[key] == 0 or weight[key] > w:
        weight[key] = w


dists = [INF]*(V+1)
dists[K] = 0
h = [(0,K)]
while h:
    d, cur = heappop(h)
    if d > dists[cur]: continue # outdated
    for nxt in nxts[cur]:
        if dists[nxt] > dists[cur] + weight[(cur,nxt)]:
            dists[nxt] = dists[cur] + weight[(cur,nxt)]
            # q.append(nxt)
            heappush(h, (dists[nxt], nxt))
    
for d in dists[1:]:
    if d != INF:
        print(d)
    else:
        print("INF")
