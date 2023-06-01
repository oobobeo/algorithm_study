# 14502

from functools import lru_cache

# complexity
# 64C3 = 41664 = doable

from itertools import combinations

N,M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

# init germs
germs = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            germs.append((i,j))

# all blank coors
blanks = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            blanks.append((i,j))
            
            
# valid neighbors
@lru_cache(maxsize=100)
def neighbors(n):
    i,j = n[0],n[1]
    result = []
    if i-1 >= 0:
        result.append((i-1,j))
    if j-1 >= 0:
        result.append((i,j-1))
    if i+1 <= N-1:
        result.append((i+1,j))
    if j+1 <= M-1:
        result.append((i,j+1))
    return result
        
        
# for all combinations
result = 0
for walls in combinations(blanks, r=3):
    # init
    temp = [l[:] for l in arr]
    for w in walls:
        temp[w[0]][w[1]] = 1
        
    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 1:
                visited[i][j] = 1
        
    # for all germs
    for g in germs:
        # init
        stack = [g]
        visited[g[0]][g[1]] = 1
        temp[g[0]][g[1]] = 2
        # DFS
        while stack:
            cur = stack.pop()
            temp[cur[0]][cur[1]] = 2
            for n in neighbors(cur):
                if visited[n[0]][n[1]] == 1: continue
                visited[n[0]][n[1]] = 1
                stack.append(n)
    
    # calculate blank space
    space = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                space += 1
    result = max(result, space)
    
print(result)






