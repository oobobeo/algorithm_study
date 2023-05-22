# 20546

N = int(input())
arr = list(map(int, input().split()))

a_m = b_m = N
bnp = 0
timing = 0
for i,a in enumerate(arr):
    while a_m >= a:
        bnp += 1
        a_m -= a

    if i >= 3:
        if arr[i] > arr[i-1] > arr[i-2] > arr[i-3]:
            b_m += timing * a
            timing = 0
        if arr[i] < arr[i-1] < arr[i-2] < arr[i-3]:
            while b_m >= a:
                timing += 1
                b_m -= a

if a_m+bnp*arr[-1] > b_m+timing*arr[-1]:
    print("BNP")
elif a_m+bnp*arr[-1] < b_m+timing*arr[-1]:
    print("TIMING")
else:
    print("SAMESAME")








