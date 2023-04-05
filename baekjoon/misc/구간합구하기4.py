# 11659








import sys


N, M = map(int, input().split())
nums = [0] + list(map(int, sys.stdin.readline().split() ))
for x in range(1,N+1):
    nums[x] = nums[x] + nums[x-1]
print(nums)
# 0'th ~ [N-1]'th
for _ in range(M):
    i,j = map(int, sys.stdin.readline().split())
    print('i','j',i,j)
    print(nums[j] - nums[i-1])

