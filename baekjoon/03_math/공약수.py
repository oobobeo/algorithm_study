# 5618

'''
문제를 잘못 이해해서 삽질을 했다.
input num 크기 순서는 랜덤.

gcd 구하는 과정 헷갈려서 또 삽질.

combination 구하는데에 product() 함수 사용.
	itertools.product(*iter)
reduce로 약수들 구함
	functools.reduce(operator.mul, iter)
'''



from collections import defaultdict
import itertools
from functools import reduce
import operator


N = int(input())


def gcd(a,b):
	r = a % b
	if r == 0:
		return b
	else: return r


if N == 2:
	l = list(map(int, input().split()))
	b,a = sorted(l)
	while 1:
		g = gcd(a,b)
		if g == b:
			break
		a = b
		b = g
if N == 3:
	l = list(map(int, input().split()))
	c,b,a = sorted(l)
	while 1:
		g_ = gcd(a,b)
		if g_ == b:
			break
		a = b
		b = g_
	while 1:
		g = gcd(c,g_)
		if g == g_:
			break
		c = g_
		g_ = g

d = defaultdict(int)
i = 2
while i <= g:
	while g % i == 0:
		g /= i
		d[i] += 1
	i += 1

vector = [[k**i for i in range(v+1)] for k,v in d.items()]
p = itertools.product(*vector)
if vector:
	result = [reduce(operator.mul, x) for x in p]
	# print(result)
	for x in sorted(result):
		print(x)
else:
	print(1)


