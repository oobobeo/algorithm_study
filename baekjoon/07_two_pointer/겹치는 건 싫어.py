# 20922

import sys

N,K = map(int, input().split())

arr = list(map(int, sys.stdin.readline().split())) # len = N

counts = [0]*(100001)
st,en = 0,0
counts[arr[0]] = 1
record = 0
while en <= N-2:
    # print(st,en, counts)
    target = arr[en+1]
    if counts[target] == K: # limit
        while True:
            cur = arr[st]
            counts[cur] -= 1
            st += 1
            if cur == target: break
    else:
        en += 1
        counts[arr[en]] += 1
    record = max(record, en-st+1)
print(record)









