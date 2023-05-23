# 21608

from collections import defaultdict

N = int(input())
arr = []
like = {}
for _ in range(N**2):
    eq = list(map(int, input().split()))
    arr.append(eq)
    like[eq[0]] = eq[1:]

# resulting placements
r = [[0]*N for _ in range(N)]

# valid
def valid(x,y):
    if x < 0 or x > N-1 or y < 0 or y > N-1:
        return False
    return True


# likes -> cands(unique)
history = []
def make_cand(poses):
    # print('history', history)
    if len(poses) == 0: return []
    cand = []
    for num,p in poses:
        if num not in history: continue
        cand.append((p[0]+1,p[1]))
        cand.append((p[0]-1,p[1]))
        cand.append((p[0],p[1]+1))
        cand.append((p[0],p[1]-1))
    cand =  [c for c in cand if valid(c[0],c[1]) and r[c[0]][c[1]] == 0]

    max_num = 0
    d = defaultdict(int)
    for c in cand:
        d[c] += 1
        max_num = max(max_num, d[c])

    cand = []
    for k,v in d.items():
        if v == max_num:
            cand.append(k)
    return list(set(cand))

# cond2
# 인접칸의 빈칸 비율 많은 칸
def fsort2(l):
    if len(l) == 0:
        for i in range(N):
            for j in range(N):
                if r[i][j] == 0:
                    l.append((i,j))

    max_num = 0
    blanks = defaultdict(int) # blanks[(1,2)] = 3
    for p in l:
        x,y = p[0],p[1]
        if valid(x+1,y) and r[x+1][y] == 0: blanks[(x,y)] += 1
        if valid(x-1,y) and r[x-1][y] == 0: blanks[(x,y)] += 1
        if valid(x,y+1) and r[x][y+1] == 0: blanks[(x,y)] += 1
        if valid(x,y-1) and r[x][y-1] == 0: blanks[(x,y)] += 1
        max_num = max(max_num, blanks[(x,y)])

    result = []
    for k,v in blanks.items():
        if v == max_num:
            result.append(k)
    return result


# cond3
# l is gauranteed to be multiple
# sortby(row, col)
def fsort3(l):
    return sorted(l)



pos = defaultdict(tuple) # pos[4] = (1,2)
for cmd in arr:
    x = cmd[0]
    a,b,c,d = cmd[1:]
    history.append(x)

    poses = [(p,pos[p]) for p in cmd[1:] if pos[p] != None]
    cand = make_cand(poses)
    # print(x, 'cand1', cand)


    if len(cand) == 1:
        r[cand[0][0]][cand[0][1]] = x
        pos[x] = (cand[0][0],cand[0][1])
        continue
    else: # len = 0 or 2+
        cand = fsort2(cand) # generated if len = 0
        if len(cand) == 1:
            r[cand[0][0]][cand[0][1]] = x
            pos[x] = (cand[0][0],cand[0][1])
            continue
        else: # multiple cands
            cand = fsort3(cand)
            # print(x, 'cand2', cand)
            r[cand[0][0]][cand[0][1]] = x
            pos[x] = (cand[0][0],cand[0][1])

    # for rrrr in r:
    #     print(rrrr)




# # calculate satis
satis = 0
for i in range(N):
    for j in range(N):
        s = 0
        if valid(i+1,j) and r[i+1][j] in like[r[i][j]]: s+= 1
        if valid(i-1,j) and r[i-1][j] in like[r[i][j]]: s+= 1
        if valid(i,j+1) and r[i][j+1] in like[r[i][j]]: s+= 1
        if valid(i,j-1) and r[i][j-1] in like[r[i][j]]: s+= 1
        if s == 0:
            satis += 0
        else:
            satis += 10**(s-1)
print(satis)



