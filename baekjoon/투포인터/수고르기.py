# 2230

import sys
import bisect

N, M = map(int, input().split())
l = []
for _ in range(N):
    # bisect.insort(l, int(sys.stdin.readline()))
    l.append(int(sys.stdin.readline()))
l.sort()

min = 2_000_000_000
st = en = 0
while True:
    # exit
    if st >= N or en >= N: break

    # check st,en
    diff = l[en] - l[st]
    if diff >= M and diff < min:
        min = diff

    # update st,en
    if diff < M:
        en += 1
    else:
        st += 1

print(min)