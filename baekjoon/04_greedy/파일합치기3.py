# 13975

'''
증명은 모르겠다.
'허프만 인코딩'이라는 기법이라고 한다.
그냥 감으로 풀었다.

'''

import sys
from heapq import *


T = int(input())
for _ in range(T):
    K = int(input())
    h = []
    arr = list(map(int, sys.stdin.readline().split()))
    while arr:
        heappush(h,arr.pop())
    total = 0
    while len(h) >= 2:
        a,b = heappop(h),heappop(h)
        total += (a+b)
        heappush(h,a+b)
    print(total)









