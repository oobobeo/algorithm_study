# 21279

'''
알고리즘 분류에 '두 포인터', '우선순위 큐'가 있어서 엄청난 힌트를 얻어서 풀었다.

중간에 구현 좀 잘못한것 때문에 몇번 틀렸다.
<sol>
좌표 범위가 너무 크기 떄문에 dp는 불가능.
광물개수도 너무 많아서 무조건 O(N)으로 풀어야된다.

꼭지점의 한부분이 (0,0)으로 고정 돼있으므로  (x=i, y=j) 이면 직사각형이 고정된다.
i=min(xs) 부터시작, j=max(ys) 부터 시작해서,
파산되기 전까지 i를 늘린다. 파산이 됐으면 j를 최소한으로 줄이고,
다시 그 j값을 사용하면서 i를 최대한 늘리는 것을 반복하면
    "최대한 많은 광물을 포함하는 직사각형"들을 구할 수 있다.
    이 직사각형들에 있는 광물들의 value합을 기록하고, 마지막에 최대value값을 print.

note1)
    직사각형에 들어있는 광물을 y값이 큰 순서로 O(1)로 pop해줘야 되므로
    max_heap을 사용해야된다.
note2)
    처음에 col[x] = []에 광물들을 y값에 대한 min_heap으로 구현해 줬는데, 이러면
    1. 현재_직사각형(cur_y2v)에 넣을때 (y<=j)까지만 넣는것을 구현가능
    2. 애초에 col[x] populate할떄 heappush 하므로 O(logN)으로
        col[x] update 가능
        cf) list.sort, bisect.insort 하면 col[x]만드는게 O(Nlog)이 넘어간다.
'''

import sys
from collections import defaultdict
from heapq import *

N, C = map(int, input().split())


# init
ys = set()
xs = set()
cols = defaultdict(list) # cols[x]=[(y,v), ..] # min_heap
# rows = defaultdict(list)
value = {}
for _ in range(N):
    x,y,v = map(int, sys.stdin.readline().split())
    xs.add(x)
    ys.add(y)
    heappush(cols[x], (y,v))
    # h.heappush(rows[y], (-x,v))
xs = sorted(list(xs))
ys = sorted(list(ys))

# print(xs,ys,cols)

# 2_pointer
# for square [0~i][0~100_000-j]
cur_y2v = [] # (-y,v), max_heap for popping when j decreases
count = 0
value = 0
values = [0]
j = ys.pop() # j 까지 먹음
imp_flag = False
for i in xs:    
    while cols[i] and cols[i][0][0] <= j:
        yy,vv = heappop(cols[i])
        value += vv
        heappush(cur_y2v, (-yy, vv))
        count += 1
        # print(cur_y2v)
        # print('aaaaaaa')

    while count > C:
        while cur_y2v and -cur_y2v[0][0] >= j:
            _, v = heappop(cur_y2v)
            value -= v
            count -= 1
        # print(1, cur_y2v, ys, j)
        if len(ys) == 0:
            imp_flag = True
            break
        j = ys.pop()
    
    # value = max(prev_value, value)
    values.append(value)
    if imp_flag:
        break
    # print(value, cur_y2v)

print(max(values))   


