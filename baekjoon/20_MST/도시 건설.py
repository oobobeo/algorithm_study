# 21924

import sys

N, M = map(int, input().split())

edges = []
total = 0
for _ in range(M):
    a,b,c = map(int, sys.stdin.readline().split())
    edges.append((c,a,b))
    total += c
edges.sort()

parent = [i for i in range(N+1)]
rank   = [0]*(N+1)
def find(x):
    if x == parent[x]:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a == b:
        return True
    else:
        if rank[a] > rank[b]:
            parent[b] = a
        elif rank[a] < rank[b]:
            parent[a] = b
        else:
            parent[a] = b
            rank[b] += 1
        return False

# kruskal
tree = []
for c,a,b in edges:
    if union(a,b): continue
    else:
        tree.append(c)
    if len(tree) == N-1: break

if len(tree) != N-1: # there are 2+ separation
    print(-1)
else:
    print(total - sum(tree))


