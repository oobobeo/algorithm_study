# 1764

# set.intersection(): O(N) = min(len(s1), len(s2))

import sys


N,M = map(int, input().split())

a = set()
b = set()
for _ in range(N):
    a.add(sys.stdin.readline().strip())
for _ in range(N):
    b.add(sys.stdin.readline().strip())

c = list(a.intersection(b))
c.sort()
print(len(c))
for cc in c:
    print(cc)
