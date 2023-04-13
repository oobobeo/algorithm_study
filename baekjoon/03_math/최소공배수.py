# 1934

'''
LCM = AxB/GCD
'''


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
    A,B = map(int, input().split())
    print(A*B//gcd(A,B))






