# 2212

'''
행복유치원 과 같은 문제
문제설명이 난해했서 질문게시판을 보고 풂.
'''

import sys


N = int(input())
K = int(input())
arr = list(map(int, sys.stdin.readline().split()))


arr = sorted(arr)
diff = []
for i in range(1,len(arr)):
    diff.append(arr[i]-arr[i-1])
diff_sorted = sorted(diff)
max_diff = diff_sorted[-K+1:]


# print(arr[-1]-arr[0]-sum(max_diff))
# ans = arr[-1]-arr[0]
# for i in range(N-2,N-K-1,-1):
#     ans -= diff_sorted[i]
# print(ans)
print(sum(diff_sorted[:N-K]))








