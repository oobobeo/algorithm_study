# 15787

import sys

N,M = map(int, input().split())

arr = [[0]*20 for _ in range(N)]
for _ in range(M):
    eq = list(map(int, sys.stdin.readline().split()))
    if eq[0] == 1:
        arr[eq[1]-1][eq[2]-1] = 1
    elif eq[0] == 2:
        arr[eq[1]-1][eq[2]-1] = 0
    elif eq[0] == 3:
        for i in range(18,-1,-1):
            arr[eq[1]-1][i+1] = arr[eq[1]-1][i]
        arr[eq[1]-1][0] = 0
    else:
        for i in range(0,19):
            arr[eq[1]-1][i] = arr[eq[1]-1][i+1]
        arr[eq[1]-1][19] = 0
    
    # for l in arr:
    #     print(l)
    # print('---------------------')
        
s = set()
for i in range(N):
    t = 0
    for j in range(20):
        t += (2**j)*arr[i][j]
    s.add(t)
print(len(s))


# for l in arr:
#     print(l)









