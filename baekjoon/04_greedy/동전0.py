# 11047

import sys

N,K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline().strip()))

result = 0
while coins and K:
    x = coins.pop()
    if x <= K:
        n = K//x
        result += n
        K -= n*x
print(result)







