# 16918


R, C, N = map(int, input().split())

arr = []
for _ in range(R):
    arr.append(list(input()))
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'O':
            arr[i][j] = 0

# time % 3 == 0
def set_bomb(time):
    for i in range(R):
        for j in range(C):
            if arr[i][j] == '.':
                arr[i][j] = time
                
                
def explode(x,y,time):
    arr[x][y] = '.'
    if x-1 >= 0:
        if arr[x-1][y] == time-1:
            arr[x-1][y] = '.'
        # if arr[x-1][y] < time-1:
        #     arr[x-1][y] = '*'
    if x+1 <= R-1:
        if arr[x+1][y] == time-1:
            arr[x+1][y] = '.'
        # if arr[x+1][y] < time-1:
        #     arr[x+1][y] = '*'
    if y-1 >= 0:
        if arr[x][y-1] == time-1:
            arr[x][y-1] = '.'
        # if arr[x][y-1] < time-1:
        #     arr[x][y-1] = '*'
    if y+1 <= C-1:
        if arr[x][y+1] == time-1:
            arr[x][y+1] = '.'
        # if arr[x][y+1] < time-1:
        #     arr[x][y+1] = '*'

def explode_bomb(time):
    for i in range(R):
        for j in range(C):
            if arr[i][j] != '.' and arr[i][j] < time-1:
                explode(i, j, time)
    
    
for i in range(1,N+1):
    if i == 1:
        continue
    if i % 2 == 0:
        set_bomb(i)
    if i % 2 == 1:
        explode_bomb(i)
    
    # print(i)
    # for a in arr:
    #     a = ''.join(list(map(str, a)))
    #     # print(*a.replace(str(N-1),'O'))
    #     print(a)
    # print()
        
for a in arr:
    a = ''.join(list(map(str, a)))
    a = a.replace(str(N),'O')
    a = a.replace(str(N-1),'O')
    a = a.replace(str(N-2),'O')
    a = a.replace(str(N-3),'O')
    print(*a, sep='')
