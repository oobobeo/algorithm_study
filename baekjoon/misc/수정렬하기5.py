# 15688
import sys

arr = [0]*2_000_004

N = int(input())

for _ in range(N):
    n = int(sys.stdin.readline().strip())
    arr[n+1_000_000] += 1

for i in range(2_000_004):
    if arr[i] == 0:
        continue
    for _ in range(arr[i]):
        print(i-1_000_000)

