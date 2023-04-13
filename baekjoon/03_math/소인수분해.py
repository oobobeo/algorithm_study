# 11653






N = int(input())


i = 2
while N > 1:
    while N % i == 0:
        print(i)
        N /= i
    i += 1
        



