# 11053

'''
처음에 tree로 풀려고 했는데 너무 복잡해서 답을 찾아봤다.
LIS(Longest Increasing Subsequence) 알고리즘으로 푸는 문제였다.
'''

import bisect

N = int(input())
A = list(map(int, input().split()))

L = []

for x in A:
    if len(L) == 0 or L[-1] < x:
        L.append(x)
    else:
        idx = bisect.bisect_left(L,x)
        L[idx] = x

print(len(L))






