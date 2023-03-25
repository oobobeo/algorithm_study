

















import sys
from collections import deque


N, M = map(int, input().split())

indegree = [0]*(N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    indegree[b] += 1
    graph[a].append(b)

order = []
q = deque()
for i in range(1,N+1):
    if indegree[i] == 0: q.append(i)
while q:
    curr = q.popleft()
    order.append(curr)
    for i in graph[curr]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

order = map(str, order)
print(' '.join(order))

