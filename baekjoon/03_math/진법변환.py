# 5618




N,B = input().split()
N = list(N)
B = int(B)

result = 0

for i,x in enumerate(N[::-1]):
	if x.isalpha():
		result += (B**i)*(ord(x)-55)
	else:
		result += (B**i)*int(x)

print(result)




