# 16234

'''
길다!
'''

from collections import defaultdict

N,L,R = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

def nei(i,j):
    result = []
    if i-1 >= 0:
        result.append((i-1,j))
    if i+1 <= N-1:
        result.append((i+1,j))
    if j-1 >= 0:
        result.append((i,j-1))
    if j+1 <= N-1:
        result.append((i,j+1))
    return result


def flow():
    global arr
    # cor2g = [[-1]*N for _ in range(N)] # cor2g[i][j] = 1
    conn = defaultdict(list)
    temp = [l[:] for l in arr]
    # print(temp)
    changed = True
    
    for i in range(N):
        for j in range(N):
            neighbors = nei(i,j)
            for n in neighbors:
                diff = abs(arr[n[0]][n[1]] - arr[i][j]) 
                if diff >= L and diff <= R:
                    conn[(n[0],n[1])].append((i,j))
                    conn[(i,j)].append((n[0],n[1]))
    
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j]: continue
            if conn[(i,j)]:
                stack = [(i,j)]
                group = []
                while stack:
                    cur = stack.pop()
                    group.append(cur)
                    visited[cur[0]][cur[1]] = 1
                    for c in conn[(cur[0],cur[1])]:
                        if visited[c[0]][c[1]] == 0:
                            stack.append(c)
                group = list(set(group))
                
                # print('g', group)
                group_total = 0
                for node in group:
                    group_total += arr[node[0]][node[1]]
                for node in group:
                    temp[node[0]][node[1]] = group_total // len(group)
    
    # check for change
    # print(temp)
    changed = (temp == arr)
    arr = [l[:] for l in temp]
    return changed


for counter in range(2010):
    if flow(): # converged
        break

print(counter)
