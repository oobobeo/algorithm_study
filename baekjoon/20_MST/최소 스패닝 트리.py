# 1197

# MST, kruskal(크루스칼)

V,E = map(int, input().split())

edges = []
for _ in range(E):
    a,b,c = map(int, input().split())
    edges.append((c,a,b))
edges.sort()

parent = [i for i in range(V+1)]
rank   = [0]*(V+1)
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
    
count = 0
ans = 0
for edge in edges:
    c,a,b = edge
    if union(a,b):
        continue
    else:
        count += 1
        ans += c
    if count == V-1:
        break

print(ans)










