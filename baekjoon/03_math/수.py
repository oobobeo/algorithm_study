# 22943

'''
백준문제가 가끔 그렇듯, 명확하지 않은 조건이 있다.
2번 cond가 헷갈리게 적혀있어서 삽질 했다.
'''

import itertools

K,M = map(int, input().split())

def cond1(n):
    for i in range(2,n//2 +1):
        if prime[i] and prime[n-i] and i != n-i:
            return True
    return False

# 나머지가 0일때까지 나눔
def cond2(n):
    while n%M == 0:
        n = n//M
        
    i = 2
    while i*i <= n:
        if prime[i]:
            j = n // i
            if n%i == 0 and prime[j]:
                return True
        i += 1
    return False


# 100mb
prime = [1]*(100_001)
prime[1] = 0
for i in range(2,317):
    j = i**2
    while j <= 100_000:
        prime[j] = 0
        j += i

count = 0
nums = '0123456789'
# c = [print(''.join(x)) for x in itertools.permutations(nums, K) if x[0] != '0']
c = [int(''.join(x)) for x in itertools.permutations(nums, K) if x[0] != '0']
for num in c:
    # print(num, cond1(num), cond2(num))
    if cond1(num) and cond2(num):
        count += 1
print(count)







