# 14425
# input -> sys.stdin.readline().strip()

import sys
def input():
    return sys.stdin.readline().strip()

n,m = map(int, input().split())

s = set()
for _ in range(n):
    s.add(input())

counter = 0
for _ in range(m):
    if input() in s:
        counter += 1

print(counter)
