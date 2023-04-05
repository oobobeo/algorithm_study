# 10816












import sys
import bisect


N = int(input())
l = []
line = list( map(int,sys.stdin.readline().split()) )
# for i in range(N):
#     bisect.insort(l, line[i])
l = sorted(line)

M = int(input())
line = list( map(int,sys.stdin.readline().split()) )
result = []
for i in range(M):
    left = bisect.bisect_left(l, line[i])
    right = bisect.bisect_right(l, line[i])
    result.append(right-left)

result = [str(i) for i in result]
print(' '.join(result))


