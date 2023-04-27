# 11399



N = int(input())
n = list(map(int, input().split()))
n.sort()

result = 0
for i,x in enumerate(n):
    result += x*(N-i)
print(result)






