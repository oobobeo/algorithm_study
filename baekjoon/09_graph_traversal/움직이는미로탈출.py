# 16954

'''
O(9^8)=4304_6721 정도
'''

from functools import lru_cache
from collections import deque

arr = []
for _ in range(8):
    arr.append(list(input()))

arr_t = [] # arr_t[8][8][8], arr_t[t] = 8x8
for t in range(8):
    # arr_t[t]
    # update temp
    temp = [['.']*8 for _ in range(8)]
    for i in range(7,0,-1): # 크게 상관 x
        for j in range(8):
            if arr[i][j] == '#' or arr[i-1][j] == '#':
                temp[i][j] = '#'
    
    # push down arr
    for i in range(7,0,-1):
        for j in range(8):
            if arr[i-1][j] == '#':
                arr[i][j] = '#'
            else: 
                arr[i][j] = '.'
    for j in range(8):
        arr[t][j] = '.'
        
    # add slice to arr_t
    arr_t.append([l[:] for l in temp])

# coor = (7,0)
# end = (0,7)
# moves = [stay, move 1, move diag] # 9 ways

@ lru_cache(maxsize=100)
def next(coor):
    x,y = coor
    result = [(x-1,y-1),(x-1,y),(x-1,y+1),\
              (x,y-1),(x,y),(x,y+1),\
                (x+1,y-1),(x+1,y),(x+1,y+1)]
    return [c for c in result if\
             c[0] >= 0 and c[0] <= 7 and c[1] >= 0 and c[1] <= 7]

q = deque([(7,0,0)]) # (x,y,t)
while q:
    cur = q.popleft()
    # print(cur)
    # if len(q) >= 3: break
    x,y,t = cur
    if t == 7:
        print(1)
        exit(0)
    for n in next((x,y)):
        if arr_t[t][n[0]][n[1]] == '#': continue
        q.append((*n,t+1))

print(0)
