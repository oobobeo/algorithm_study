# 16562

N,M,k = map(int, input().split())

cost = [0]+list(map(int, input().split()))

parent = [i for i in range(N+1)]
rank   = [1]*(N+1)
roots = set(parent)

def find(x):
    if x == parent[x]:
        return x
        
    else:
        y = find(parent[x])
        cost[y] = min(cost[y], cost[x])
        parent[x] = y
        return y

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return
    
    if rank[x] < rank[y]:
        roots.remove(x)
        parent[x] = y
    elif rank[x] > rank[y]:
        roots.remove(y)
        parent[y] = x
    elif rank[x] == rank[y]:
        roots.remove(y)
        parent[y] = x
        rank[x] += 1

for _ in range(M):
    union(*tuple(map(int, input().split())))

# reduce height for all
for _ in range(2):
    for i in range(N+1):
        find(i)

total_cost = 0
for i,p in enumerate(parent):
    if p not in roots: continue # already accounted for
    
    total_cost += cost[p]
    roots.remove(p)

if total_cost <= k:
    print(total_cost)
else:
    print("Oh no")
