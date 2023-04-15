# 1747

def is_pal(x):
    x = str(x)
    for i in range(len(x)//2 + 1):
        if x[i] != x[-1-i]:
            return False
    return True

N = int(input())


# 100mb
prime = [1]*(2_000_001)
prime[1] = 0
for i in range(2,1415):
    j = i**2
    while j <= 2_000_000:
        prime[j] = 0
        j += i

n = N
while True:
    if prime[n] and is_pal(n):
        print(n)
        exit(0)
    n += 1
