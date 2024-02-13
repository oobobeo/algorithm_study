# 14567

import sys
from collections import defaultdict

N,M = map(int, input().split())

nxts = defaultdict(list)
indeg = [0]*(N+1)
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    indeg[b] += 1
    nxts[a].append(b)

done = [0]*(N+1)
ans = [-1]*(N+1)
time = 1
while sum(indeg) != 0:
    cur_group = []
    indeg_freeze = indeg[:]
    for i in range(len(indeg_freeze)):
        if i == 0: continue
        if indeg_freeze[i] == 0 and done[i] == 0:
            done[i] = 1
            # print('a', i, indeg)
            cur_group.append(i)
            ans[i] = time
            
            for nxt in nxts[i]:
                indeg[nxt] -= 1
    time += 1
    # if sum(indeg) < -2: break
for i in range(len(ans)):
    if ans[i] == -1:
        ans[i] = time

print(*ans[1:])
