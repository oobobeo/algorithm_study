# 22862

'''
case1) len(arr) = 1
case2) arr에 홀수의 개수가 K 미만이 경우

위 두경우를 고려해주지 못해서 틀렸다.
'''


import sys

N,K = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))

# longest subarray containing (odd numbers < k)

# init
st, en = 0,0
odd_count = 0
result = 1
if arr[0] % 2 == 1:
    odd_count = 1
    result = 0

# two-pointer
while en <= N-2:
    en += 1
    next = arr[en]
    if next % 2 == 1:
        if odd_count == K:
            while True:
                st += 1
                if arr[st-1] % 2 == 1: break
        else: # odd_count < K
            odd_count += 1
    result = max(result, en-st+1)
    # print(st, en, result)
print(result-odd_count)








