# 21920

from functools import reduce

import sys

def gcd(A,B):
    a = max(A,B)
    b = min(A,B)
    while True:
        a_ = a%b
        if a_ == 0:
            return b
        a = b
        b = a_


N = int(input())

A = list(map(int, sys.stdin.readline().split()))
X = int(input())

result = []
for a in A:
    if gcd(a,X) == 1:
        result.append(a)

print(reduce(lambda x,y: x+y, result) / len(result))
