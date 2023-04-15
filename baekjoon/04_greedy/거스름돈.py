# 14916

N = int(input())

count = 0

if N == 1 or N == 3:
    print(-1)
    exit(0)

while True:
    if N % 5 == 0:
        break
    N -= 2
    count += 1
count += N // 5
print(count)
