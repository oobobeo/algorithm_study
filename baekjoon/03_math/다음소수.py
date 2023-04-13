# 4134





def is_prime(n):
    if n == 1 or n == 0: return False
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True

T = int(input())

for _ in range(T):
    n = int(input())
    while not is_prime(n):
        n += 1
    print(n)
    