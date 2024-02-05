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
    # weight[(d,e)] = l
    # weight[(e,d)] = l

# dijkstra x 3 -> zip, min -> max
total_dists = []
for start in [A,B,C]:
    dists = [inf] * (N+1)
    dists[start] = 0
    h = [(0, start)]

    while h:
        d, cur = heappop(h)
        if d > dists[cur]: continue # outdated

        for nxt in nxts[cur]:
            if dists[nxt] > dists[cur] + weight[(cur,nxt)]:
                dists[nxt] = dists[cur] + weight[(cur,nxt)]
                heappush(h, (dists[nxt], nxt))
    total_dists.append(dists)
    # distance = [inf]*(N+1)
    # distance[start] = 0
    # pq = []
    # heappush(pq, (0, start))
    # while pq:
    #     dist, now = heappop(pq)
    #     if distance[now] < dist:
    #         continue
        
    #     for next, cost in nxts[now]:
    #         if cost + dist < distance[next]:
    #             distance[next] = cost + dist
    #             heappush(pq, (cost+dist, next))
                
    # total_dists.append(distance)

mins = []
for i,x in enumerate(zip(*total_dists)):
    if i == 0: continue
    mins.append(min(x))

target = max(mins)
for i, m in enumerate(mins):
    if m == target:
        print(i + 1)
        break
