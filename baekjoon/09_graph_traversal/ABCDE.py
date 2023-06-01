# 13023

'''
답보고 풀었다.
<sol>
재귀dfs(찐 dfs) + [dfs(x) 끝나면 visited[x] = 0]를 사용해야된다.
stack이용한 dfs는 bfs섞인 dfs여서 항상 depth first 가 아니다.

root에서 시작하는 가능한 모든 route을 다 찾는다.
loop 때문에 O(NM)은 훨씬 넘을거 같은데 시간안에 통과는 한다. (N,M = 2000)
아마 depth=5로 짧아서 graph가 complex해도 중간에 exit할 수 있어서 그런듯.
'''

from collections import deque, defaultdict

# find
# len=4인 line o-o-o-o-o

# 어딜 root로 잡아도 됨.
# 근데 loop 있음.


# (any)bfs -> (deepest)bfs?

con = defaultdict(list)
N,M = map(int, input().split())
for _ in range(M):
    a,b = map(int, input().split())
    con[a].append(b)
    con[b].append(a)
    
    
def dfs(x, visited):
    d = dist[x]
    if d == 4:
        print(1)
        exit(0)
    for n in con[x]:
        if visited[n] == 0:
            visited[n] = 1
            dist[n] = d+1
            dfs(n, visited)
            visited[n] = 0
    
    
    
for st in range(N):
    stack = [st]
    visited = [0]*N
    visited[st] = 1
    dist = [0]*N
    # dfs
    dfs(st, visited)
    
    # print(st, dist)

print(0)
