# 1758


# 8시: 줄
# 커피1개 -> 자리
# tip = x - n + 1, 음수:x


import sys

N = int(input())
tip = []
for _ in range(N):
    tip.append(int(sys.stdin.readline().strip()))
tip.sort()
tip.reverse()
result = 0
for i,x in enumerate(tip):
    if i >= x:
        break
    result = result + x - i
print(result)











