# 22865

'''
node 사이 edge가 두개 이상 있을수 있다..
하루 종일 디버깅했다. 기억하자
'''

import sys
from collections import defaultdict
from heapq import *
from math import inf

N = int(input())
A, B, C = map(int, input().split())
M = int(input())

nxts = defaultdict(list)
weight = defaultdict(lambda: inf)
for _ in range(M):
    d,e,l = map(int, sys.stdin.readline().split())
    nxts[d].append((e,l))
    nxts[e].append((d,l))
    weight[(d,e)] = l # <- WRONG
    weight[(e,d)] = l # <- WRONG
print(weight)
# dijkstra x 3 -> zip, min -> max
total_dists = []
for start in [A,B,C]:
    dists = [inf] * (N+1)
    dists[start] = 0
    h = [(0, start)]

    while h:
        d, cur = heappop(h)
        if d > dists[cur]: continue # outdated

        for nxt, cost in nxts[cur]:
            if dists[nxt] > dists[cur] + weight[(cur,nxt)]:
                dists[nxt] = dists[cur] + weight[(cur,nxt)]
                heappush(h, (dists[nxt], nxt))
    total_dists.append(dists)

mins = []
for i,x in enumerate(zip(*total_dists)):
    if i == 0: continue
    mins.append(min(x))

target = max(mins)
for i, m in enumerate(mins):
    if m == target:
        print(i + 1)
        break
