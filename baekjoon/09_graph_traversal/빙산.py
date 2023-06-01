# 2573

'''
시간복잡도 맞으면 code를 조금 optimize해주면 time limit통과하는듯 하다.
'''

from functools import lru_cache

N,M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))


# ices = [(i,j), ..]    
ices = set()
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0:
            ices.add((i,j))


# return valid neighbors
d = [(-1,0),(1,0),(0,-1),(0,1)]
@lru_cache(maxsize=90000)
def neighbors(i,j):
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

# update arr
def melt():
    global arr
    global ices
    
    # init
    temp = []
    for l in arr:
        temp.append(l[:])
    
    # update temp
    for i in range(N):
        for j in range(M):
            val = temp[i][j]
            if val == 0:
                continue
            nn = neighbors(i,j)
            score = 0
            for x,y in nn:
                if arr[x][y] == 0:
                    score += 1
            val -= score
            temp[i][j] = max(0, val)
            if temp[i][j] == 0:
                ices.discard((i,j))
    
    # update arr <- temp
    arr = []
    for ll in temp:
        arr.append(ll[:])


# check for seperated ice group
# len(ices)>0 should be gauranteed
def check_sep():
    temp = ices.copy() # 사실 그냥 ices 써도됨
    stack = [temp.pop()]
    visited = [[0]*M for _ in range(N)]
    visited[stack[0][0]][stack[0][1]] = 1
    while stack:
        cur = stack.pop()
        temp.discard(cur)
        for n in neighbors(cur[0],cur[1]):
            if visited[n[0]][n[1]] == 0 and arr[n[0]][n[1]]:
                visited[n[0]][n[1]] = 1
                stack.append(n)
    if temp:
        return True
    else:
        return False


# check for multiple ice groups
time = 0
nones = [[0]*M for _ in range(N)]
while arr != nones:
    chk = check_sep()
    if chk:
        print(time)
        exit(0)
    melt()
    time += 1
print(0)
