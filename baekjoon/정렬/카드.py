# 11652
import sys

input = sys.stdin.readline



N = int(input().strip())

hash = {}
for _ in range(N):
    n = int(input().strip())
    if n in hash:
        hash[n] += 1
    else:
        hash[n] = 1

max_count = 0
num = pow(2, 62)
for k,v in hash.items():
    if v == max_count:
        num = min(num, k)
    elif v > max_count:
        num = k
        max_count = v

print(num)




