# 11725
# input -> sys.stdin.readline().strip()

import sys

# BFS, DFS 로 풀면 edge=N-1 개 일떄 O(N)으로 풀수 있다고 한다.

# python3 -> pypy3 interpreter속도가 빠름


N = int(input())

# populate flows
flow = {} # {num: {num's}}
for i in range(N):
    flow[i+1] = set()
for i in range(N-1):
    a,b = map(int, sys.stdin.readline().strip().split())
    flow[a].add(b)
    flow[b].add(a)

# fill parents list
parents = [0]*N # parent of each nodes. from node1
known_nodes = {1}
curr_nodes = {1}
while curr_nodes:
    total_children = set()
    for n in curr_nodes:
        # remove self from children's flow
        children = flow[n]
        for c in children:
            flow[c].remove(n)
            parents[c-1] = n
        total_children = total_children | children

    curr_nodes = total_children


# calculate nodes' parents
for i in parents[1:]:
    print(i)




