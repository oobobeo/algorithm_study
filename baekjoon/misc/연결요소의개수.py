# 11724




import sys
N, M = map(int, input().split())

adjacent = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int, sys.stdin.readline().split())
    adjacent[u].append(v)
    adjacent[v].append(u)

visited = [0]*(N+1)
visited[0] = 1

# print(visited)
# print(adjacent)

count = 0
while 0 in visited:
    # pick root
    root = -1
    for i in range(N+1):
        if visited[i] == 0:
            root = i
            count += 1
            break
    if root == -1: # done
        break
    # dfs
    stack = [root]
    # visited[root] = 1
    while stack:
        curr = stack.pop()
        if visited[curr] == 1:
            continue
        visited[curr] = 1
        # print(curr)
        # print(visited)
        for adj in adjacent[curr]:
            if visited[adj]: continue
            stack.append(adj)
    # print(root)
    # print(visited)
    
print(count)



