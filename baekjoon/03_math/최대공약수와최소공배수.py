# 2609

a,b = map(int, input().split())

def gcd(A,B):
    a = max(A,B)
    b = min(A,B)
    while True:
        a_ = a%b
        if a_ == 0:
            return b
        a = b
        b = a_
g = gcd(a,b)
print(g, a*b//g, sep='\n')
