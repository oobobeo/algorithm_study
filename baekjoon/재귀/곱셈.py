# 1629


# a**b % c
a,b,c = map(int, input().split())

# for a,b,c
# calculate:
#   case1) b == 2n
#           a**(b/2) % c
#   case2) b == 2n+1
#           a**(b/2)*a % c
def pow(a,b,c):
    if b == 1:
        return a % c
    val = pow(a, int(b/2), c)
    val = val**2 % c
    if b%2 == 0:
        return val
    return val*a % c

print(pow(a,b,c))

