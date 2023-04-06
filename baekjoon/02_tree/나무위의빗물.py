# 17073




# Pi > 0 인 Pi들의 평균
'''
또 tree 훼이크 문제.
시뮬레이션 돌리는게 아니라 W/len(leaf) 가 답이다.

DFS로 node를 탐색하고, leaf를 색출했다.
'''

import sys
from collections import defaultdict

N,W = map(int,input().split())

adj = defaultdict(set)
# set up adj
for line in sys.stdin:
    line = line.strip()
    if not line: break
    a,b = map(int, line.split())
    adj[a].add(b)
    adj[b].add(a)

# find leafs using DFS
stack = [1]
visited = set([1])
leaf_count = 0
while stack:
    cur = stack.pop()
    adjs = [x for x in adj[cur] if x not in visited]
    visited.update(adjs)
    stack += adjs
    # are adjs leaf?
    for an in adjs:
        if adj[an].issubset(visited):
            leaf_count += 1

print(W/leaf_count)