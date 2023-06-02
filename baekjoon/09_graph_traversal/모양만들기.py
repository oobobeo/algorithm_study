# 16954

'''
(i,j)-> 로 unique gid를 (i*N+j) 로 해줬는데, (i*M+h)로 해 줬어야 했다..
chatgpt가 찾아줌 ㅎ
'''

from collections import defaultdict

N,M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

# 1. group 분류
#       group[i][j] = gid
#       전체 1에 대해 loop:
#           dfs 하면서 visited 추가(중복 방지)
# 2. 전체 loop:
#       group_size[gid] = size update.
# 3. 전체 0 에 대해 loop
#       neighbor들 의 gid 비교, 다르면 cand += (group_size1 + ..)

def neighbor(coor):
    x,y = coor
    result = []
    if x-1 >= 0 and arr[x-1][y] == 1:
        result.append((x-1,y))
    if y-1 >= 0 and arr[x][y-1] == 1:
        result.append((x,y-1))
    if x+1 <= N-1 and arr[x+1][y] == 1:
        result.append((x+1,y))
    if y+1 <= M-1 and arr[x][y+1] == 1:
        result.append((x,y+1))
    return result

group = [[-1]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]
def dfs(coor, gid):
    stack = [coor]
    visited[coor[0]][coor[1]] = 1
    while stack:
        cur = stack.pop()
        print(cur)
        group[cur[0]][cur[1]] = gid
        for n in neighbor(cur):
            if visited[n[0]][n[1]] == 0:
                stack.append(n)
                visited[n[0]][n[1]] = 1

# 1. group
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0: continue
        if visited[i][j]: continue
        print('start: ', (i,j))
        dfs((i,j), i*N+j)

# 2. group size
group_size = defaultdict(int)
for i in range(N):
    for j in range(M):
        if group[i][j] == -1: continue
        group_size[group[i][j]] += 1

for gg in group:
    print(gg)
print(group_size)



# 3. 전체 0 loop
cands = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1: continue
        gids = set()
        for n in neighbor((i,j)):
            gids.add(group[n[0]][n[1]])
        cands.append(sum([group_size[x] for x in gids]) + 1)

print(max(cands))
