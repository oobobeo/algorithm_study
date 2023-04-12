# 5618









N = int(input())


def gcd(a,b):
	r = a % b
	if r == 0:
		return b
	else: return r


if N == 2:
	b,a = map(int, input().split())
	while 1:
		g = gcd(a,b)
		if g == b:
			break
		a = b
		b = g
if N == 3:
	c,b,a = map(int, input().split())
	while 1:
		g_ = gcd(a,b)
		if g_ == b:
			break
		a = b
		b = g_
	while 1:
		g = gcd(c,g_)
		if g == b:
			break
		c = g_
		g = g


i = 2
while i <= g:
	while 



