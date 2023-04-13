# 1110







N = int(input())


n = N
count = 0
while True:
    count += 1
    if n < 10:
        a = n
        n *= 11
    else:
        a = n%10
        b = (a + n//10)%10
        n = a*10 + b

    if n == N:
        print(count)
        exit(0)




