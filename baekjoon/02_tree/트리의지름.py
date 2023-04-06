# 1967


'''
<풀이>
가장 깊은 노드는 무조건 사용됨. (귀납법으로 증명가능)
1. 가장 깊은 노드 m 찾음
2. m에서 DFS로 지름 찾음

푸는데 1시간 반정도 걸린거 같다..

'''


import sys
from collections import defaultdict

N = int(input())
adj = defaultdict(list)
child = defaultdict(list) # child[node] = [(child, d), ..]
for _ in range(N-1):
    p,n,d = map(int, sys.stdin.readline().split())
    adj[p].append((n,d))
    adj[n].append((p,d))
    child[p].append((n,d))

stack = [(1,0)] # node, depth
depth = [0]*(N+1) # depth from root
while stack:
    cur, d = stack.pop()
    if not child[cur]: # leaf
        depth[cur] = d
        continue
    for c,dd in child[cur]:
        stack.append((c,d+dd))

# find deepest node
st = depth.index(max(depth)) 

# DFS from st
stack = [(st,0)]
visited = set([st])
depth = [0]*(N+1)


print(adj)


while stack:
    cur, d = stack.pop()
    adjs = [x for x in adj[cur] if x[0] not in visited]
    if not adjs: # leaf
        depth[cur] = d
    for ad in adjs:
        stack.append((ad[0],ad[1]+d))
        visited.add(ad[0])

print(max(depth))








