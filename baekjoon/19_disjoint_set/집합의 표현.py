# 1717

# union find

import sys

N,M = map(int, input().split())

cmds = []
for _ in range(M):
    tup = tuple(map(int, sys.stdin.readline().split()))
    cmds.append(tup)

parent = [i for i in range(N+1)]
rank   = [1]*(N+1)

def find(x):
    if x == parent[x]:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return
    
    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x
    elif rank[x] == rank[y]:
        parent[y] = x
        rank[x] += 1

for op,a,b in cmds:
    if op == 0:
        union(a,b)
    elif op == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")






