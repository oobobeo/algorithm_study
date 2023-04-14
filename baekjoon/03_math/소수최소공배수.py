# 21919


import sys
from functools import reduce


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

prime = [1]*(1000001)
prime[1] = 0
for i in range(2,1001):
    j = i**2
    while j <= 1000000:
        prime[j] = 0
        j += i

p = set()
for a in A:
    if prime[a]:
        p.add(a)
if p:
    print(reduce(lambda x,y : x*y, p))
else:
    print(-1)

