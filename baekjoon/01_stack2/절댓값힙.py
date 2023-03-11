# 12951
# input -> sys.stdin.readline().strip()

import sys
import heapq

N = int(input())

heap = []
for i in range(N):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))







