# 1978


import sys

N = int(input())

prime = [1]*(1001)
prime[1] = 0
for i in range(2,32):
	j = i**2
	while j <= 1000:
		prime[j] = 0
		j += i
# print(prime[1:])
count = 0
for x in map(int, sys.stdin.readline().split()):
	if prime[x]:
		count += 1
print(count)
