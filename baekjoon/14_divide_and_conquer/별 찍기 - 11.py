# 2448

N = int(input())
k = N//3
iter = 0
while True:
    if 2**iter == k:
        break
    iter += 1

base = [[' ',' ','*',' ',' '],
        [' ','*',' ','*',' '],
        ['*','*','*','*','*']]

for i in range(1,iter+1):
    side = 3*(2**(i-1))
    R = side*2
    C = R*2-1
    new_base = [[' ']*C for _ in range(R)]
    for x,y in [(0,side),(side,0),(side,side*2)]: # offset
        for i in range(side):
            for j in range(side*2-1):
                new_base[x+i][y+j] = base[i][j]
    base = new_base

for l in base:
    print(''.join(map(str,l)))
