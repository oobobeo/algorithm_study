# 9613

from itertools import combinations
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

T = int(input())

for _ in range(T):
    nums = list(map(int, input().split()))
    c = combinations(nums[1:], r=2)
    result = []
    for g in c:
        result.append(gcd(*g))
    print(reduce(lambda x,y: x+y, result))


