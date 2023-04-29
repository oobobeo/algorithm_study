# 20300

import sys

N = int(input())
loss = list(map(int, sys.stdin.readline().split()))
loss.sort()

m = []
if N % 2 == 1:
    m.append(loss.pop())
for i in range(N//2):
    m.append(loss[i] + loss[(N//2)*2-1-i])
m.sort()
print(m[-1])




