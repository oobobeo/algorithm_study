# 1277

'''
floating point operation 에서 소숫점은 precision이 떨어진다.
소숫점 floating point의 대소비교는 (100% 정확하게는) 불가
'''

import math
from collections import defaultdict
from heapq import *

N, W = map(int, input().split())
M = float(input())

coor = {}
for i in range(N):
    x,y = map(float, input().split())
    coor[i+1] = (x,y)

exists = defaultdict(int)
for _ in range(W):
    a,b = map(int, input().split())
    exists[(a,b)] = 1
    exists[(b,a)] = 1
    
dists = defaultdict(lambda: float("inf")) # dists[(a,b)] = float
for a in range(1,N+1):
    for b in range(1,N+1):
        if a == b: continue
        d = math.dist(coor[a], coor[b])
        d2 = (coor[a][0]-coor[b][0])**2 + (coor[a][1]--coor[b][1])**2
        if d > M**2: continue # 이부분 유의!!!!
        if exists[(a,b)] == 1:
            d = 0
        dists[(a,b)] = d
        dists[(b,a)] = d

neighbors = defaultdict(list)
for a in range(1,N+1):
    for b in range(a+1,N+1):
        if dists[(a,b)] <= M:
            neighbors[a].append(b)
            neighbors[b].append(a)
            
# dijkstra
h = [(0,1)]
acc_dist = [float("inf")]*(N+1)
acc_dist[1] = 0
while h:
    d, cur = heappop(h)
    if d > acc_dist[cur]: continue # outdated
    
    for nei in neighbors[cur]:
        if acc_dist[nei] > acc_dist[cur] + dists[(cur,nei)]:
            acc_dist[nei] = acc_dist[cur] + dists[(cur,nei)]
            heappush(h, (acc_dist[nei], nei))

print(int(1000*acc_dist[N]))










