# 20115


import sys

N = int(input())

drink = list(map(int, sys.stdin.readline().split()))

drink.sort()

total = drink.pop()

for d in drink:
    total += d/2


print(total)






