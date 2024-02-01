# 14929

import sys

N = int(input())
l = list(map(int, sys.stdin.readline().split()))

print((sum(l)**2 - (sum(map(lambda x: x**2, l))))//2)

'''
누적합을 이용해
Sigma[S-xn]*xn 으로 구할수도 있음
'''
