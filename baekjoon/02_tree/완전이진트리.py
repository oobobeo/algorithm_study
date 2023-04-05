# 9934







import sys




K = int(input())
arr = list(map(int, input().split()))

div = 2
while True:
    layer = []
    idx = len(arr) // div
    dist = idx+1
    while idx < len(arr):
        if arr[idx] != -1:
            layer.append(arr[idx])
            arr[idx] = -1
        idx += dist

    div *= 2
    print(*layer)
    if len(arr)+1 < div:
        break


