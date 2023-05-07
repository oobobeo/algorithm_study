# 11055

'''
LIS 사용하는줄 알았는데
N이 작아서 O(N^2) DP 으로도 풀렸다.
'''


import bisect

N = int(input())
A = list(map(int, input().split()))

S = [0]*1001 # idx 로 끝난는 수열중 가장 큰 합

S[A[0]] = A[0]
for x in A[1:]:
    S[x] = max(S[x], max(S[:x])+x)

print(max(S))






