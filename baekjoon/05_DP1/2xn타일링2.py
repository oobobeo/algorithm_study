# 11727

'''
점화식 구하는데 애먹음..
An+2 = f(An+1,An) 정도로 나타내 질줄 알았는데
       f(An, An-1); n 3개 차이로 나타내졌다..
'''


# An+3 = 3*An+1 + 2*An
a = [0]*1001
a[1] = 1
a[2] = 3
a[3] = 5

N = int(input())
for i in range(4, N+1):
    a[i] = 3*a[i-2] + 2*a[i-3]
print(a[N] % 10007)






