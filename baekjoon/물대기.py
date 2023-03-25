# 1368






# index
# well = 0
# node = 1~N

import sys
from heapq import *
import functools

N = int(input())

edges = []
for i in range(1,N+1):
    wc = int(sys.stdin.readline().strip())
    edges.append((wc,i,0))


parent = [i for i in range(N+1)]
def union(a,b):
    global parent
    def find(x):
        if parent[x] != x:
            return find(parent[x])
        else:
            return parent[x]
    ap = find(a)
    bp = find(b)
    if ap == bp:
        return True
    if ap < bp:
        parent[bp] = ap
    else:
        parent[ap] = bp
    return False



# hq = [] # (cost, node1, node2)
tree = []
for i in range(1,N+1):
    costs = list(map(int, sys.stdin.readline().split()))
    for j,c in enumerate(costs[i:]):
        edges.append((c,i,j+1+i))
# [(5, 1, 0), (4, 2, 0), (4, 3, 0), (3, 4, 0), 
# (2, 1, 2), (2, 1, 3), (2, 1, 4), (3, 2, 3), (3, 2, 4), (4, 3, 4)]
edges.sort()
# for each node:
#   1. connect
#   2. make well
for edge in edges:
    c,u,v = edge[0],edge[1],edge[2]
    if union(u,v): continue
    tree.append(c)
    if len(tree) == N: break
result = functools.reduce(lambda x,y: x+y, tree)

print(result)


