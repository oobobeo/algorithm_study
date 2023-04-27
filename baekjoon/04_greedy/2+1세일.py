# 11508


import sys

N = int(input())

price = []
for _ in range(N):
    price.append(int(sys.stdin.readline()))
price.sort()

result = 0
i = 1
while price:
    x = price.pop()
    if i % 3: # 1,2
        i += 1
        result += x
    else: # 3
        i = 1
print(result)












