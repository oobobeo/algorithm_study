# 2581





import sys


M,N = int(input()), int(input())


prime = [1]*(10001)
prime[1] = 0
for i in range(2,101):
	j = i**2
	while j <= 10000:
		prime[j] = 0
		j += i

total = 0
m = -1
for i in range(M,N+1):
	if prime[i]:
		total += i
		if m == -1:
			m = i
if m == -1:
	print(-1)
else:
	print(total)
	print(m)
