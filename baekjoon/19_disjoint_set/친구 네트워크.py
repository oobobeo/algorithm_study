# 4195

from collections import defaultdict

def find(x, parent):
    if x not in parent.keys():
        parent[x] = x
    
    if x == parent[x]:
        return x
    else:
        y = find(parent[x], parent)
        parent[x] = y
        return y

def union(a, b, parent, rank):
    a = find(a, parent)
    b = find(b, parent)
    
    if a == b:
        return count[a]
    
    if rank[a] < rank[b]:
        parent[a] = b
        count[b] += count[a]
        return count[b]
    elif rank[a] > rank[b]:
        parent[b] = a
        count[a] += count[b]
        return count[a]
    else:
        parent[b] = a
        count[a] += count[b]
        rank[a] += 1
        return count[a]
    

T = int(input())
ans = []
for _ in range(T):
    F = int(input())
    parent = {}
    rank = defaultdict(int)
    count = defaultdict(lambda: 1)
    
    for _ in range(F):
        a,b = input().split()
        ans.append(union(a,b,parent,rank))
        

for aa in ans:
    print(aa)




