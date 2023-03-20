# 1931





import sys

N = int(input())

ropes = []
for _ in range(N):
    ropes.append(int(input()))

ropes.sort()
ropes.reverse()
weights = []
for i,r in enumerate(ropes):
    weights.append((i+1)*r)

print(max(weights))
