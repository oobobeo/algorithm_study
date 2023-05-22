# 2753

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))

for _ in range(M):
    a,b,c = map(int, input().split())
    if a == 1:
        arr[b] = c
    elif a == 2:
        for i in range(b,c+1):
            if arr[i] == 0: arr[i] = 1
            else: arr[i] = 0
    elif a == 3:
        for i in range(b,c+1):
            arr[i] = 0
    elif a == 4:
        for i in range(b,c+1):
            arr[i] = 1
print(*arr[1:])

