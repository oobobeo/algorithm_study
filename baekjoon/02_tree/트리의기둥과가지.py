# 20924


'''
adjs{} -> adjs[n]=[n's]
1. root->기가: root -> adj 1
2. 기가->leaf: 기가 -> DFS
    stack = [node, dist]

edge cases:
    1. 기둥만
    2. 기둥 x
'''


import sys
from collections import defaultdict

N,R = map(int, input().split())
adjs = defaultdict(list)

for _ in range(N-1):
    a,b,d = map(int, sys.stdin.readline().split())
    adjs[a].append((b,d))
    adjs[b].append((a,d))

# root -> giga
giga = R
stack = [R]
visited = set([R])
dist = 0
for i in range(N-1):
    cur = stack.pop()
    adj_list = adjs[cur]
    if i == 0 and len(adj_list) >=2:
        break
    if len(adj_list) >= 3:
        giga = cur
        break
    # n,d = [x for x in adj_list if x[0] != visited]
    n,d = [x for x in adj_list if x[0] not in visited][0]
    dist += d
    visited.add(n)
    stack.append(n)

# giga -> leaf
stack = [(giga, 0)] # [(n, d), .. ]
longest = 0
while stack:
    cur, d = stack.pop()
    adj = [x for x in adjs[cur] if x[0] not in visited]
    for n in adj:
        stack.append((n[0],d+n[1]))
        visited.add(n[0])
    # is leaf
    if not adj:
        longest = max(longest, d)

print(dist,longest)
