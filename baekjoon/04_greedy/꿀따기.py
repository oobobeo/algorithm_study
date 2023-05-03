# 21758


'''
honey pot 1칸씩 옮겨서 정답 도출이 되는 부분이 나올줄 알았다.(미분가능 할줄)
아니였다.
전체 가능한 경우에 대해 다 계산 해줌.
'''


import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))


# when honey pot is in the middle
r0 = sum(arr[1:-1]) + max(arr[1:-1])
r1 = sum(arr[2:])*2
r2 = sum(arr[:-2])*2

i = 1
temp = r1
while i <= len(arr)-3:
        temp = temp + arr[i] - arr[i+1]*2
        r1 = max(r1, temp)
        i += 1
        
i = len(arr)-2
temp = r2
while i >= 2:
    temp = temp + arr[i] - arr[i-1]*2
    r2 = max(r2, temp)
    i -= 1
        
print(max(r0,r1,r2))

