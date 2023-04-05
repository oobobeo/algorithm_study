







# 2493



import sys
from heapq import *

N = int(input())

stack = sys.stdin.readline().split()
stack = [(int(x),i+1) for i,x in enumerate(stack)] # [(val, idx), ..]
h = []
result = [0]*(N+1)

for i in range(N,1,-1):
    # 1. pop -> heap
    # 2. stack[-1] vs heap
    heappush(h, stack.pop())
    next = stack[-1]
    while h:
        if h[0][0] > next[0]: break
        t = heappop(h)
        result[t[1]] = i-1

print(' '.join(map(str,result[1:])))






