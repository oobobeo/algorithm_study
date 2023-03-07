# 1620
# input -> sys.stdin.readline().strip()

import sys

n,m = map(int, input().split())

p2i = {}
i2p = {}
for i in range(n):
    name = sys.stdin.readline().strip()
    p2i[name] = i+1
    i2p[i+1] = name

for i in range(m):
    question = sys.stdin.readline().strip()
    if question.isdigit():
        print(i2p[int(question)])
    else:
        print(p2i[question])
