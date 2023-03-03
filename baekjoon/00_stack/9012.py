



iter = int(input())
for _ in range(iter):
    bias = 0
    flag = 0 # 0 = YES, 1 = NO
    for x in input():
        if x == '(':
            bias += 1
        else: # ')'
            bias -= 1
        if bias < 0:
            flag = 1
            break
    if bias != 0 or flag == 1:
        print('NO')
        continue
    else:
        print('YES')
        continue