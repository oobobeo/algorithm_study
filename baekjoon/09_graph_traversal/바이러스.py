# 2606

from collections import defaultdict

N = int(input())
M = int(input())


con = defaultdict(list)
for _ in range(M):
    a,b = map(int, input().split())
    con[a].append(b)
    con[b].append(a)

visited = set([1])
stack = [1]
while stack:
    cur = stack.pop()
    visited.add(cur)
    
    for c in con[cur]:
        if c not in visited:
            stack.append(c)
        visited.add(c)
    
print(len(visited) - 1)
