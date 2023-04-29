# 20365



import sys

N = int(input())
colors = list(sys.stdin.readline().strip())


if N == 1:
    print(1)
    exit(0)

count = {"B": 0, "R":0}
cur_color = colors.pop()
while colors and len(colors) >= 2:
    cur = colors.pop()
    if cur == cur_color:
        continue
    else:
        count[cur_color] += 1
        cur_color = cur
if cur_color != colors[0]:
    count["B"] += 1
    count["R"] += 1
else:
    count[cur_color] += 1
m = min(count["B"], count["R"])
print(m+1)
