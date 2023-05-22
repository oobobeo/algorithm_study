# 4396


N = int(input())


arr = []
for _ in range(N):
    arr.append(list(input()))
mask = []
for _ in range(N):
    mask.append(list(input()))

r = [['.']*N for _ in range(N)]

def count(i,j):
    if i < 0 or i > N-1 : return 0
    if j < 0 or j > N-1 : return 0
    if arr[i][j] == '*':
        return 1
    return 0

open_all = False
for i in range(N):
    for j in range(N):
        if mask[i][j] == '.': continue

        if arr[i][j] == '*':
            open_all = True
            r[i][j] = '*'
        else:
            c = 0
            # a b c
            # d x e
            # f g h
            c += count(i-1, j-1)  # a
            c += count(i-1, j)           # b
            c += count(i-1, j+1)# c

            c += count(i, j-1)           # d
            c += count(i, j+1)         # e

            c += count(i+1, j-1)# f
            c += count(i+1, j)         # g
            c += count(i+1, j+1)# h
            r[i][j] = c

if open_all:
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '*':
                r[i][j] = '*'

for l in r:
    print(''.join(list(map(str,l))))

