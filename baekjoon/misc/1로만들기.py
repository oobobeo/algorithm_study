table = [0]*(10**6 + 3)
table[1] = 0
x = int(input())
for i in range(2,x+1):
	table[i] = table[i-1]+1
	if i%2 == 0: table[i] = min(table[i], table[int(i/2)]+1)
	if i%3 == 0: table[i] = min(table[i], table[int(i/3)]+1)
print(table[x])