# 20053

import sys

T = int(input())

for _ in range(T):
    N = input()
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    print(arr[0], arr[-1])
