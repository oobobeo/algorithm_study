# 15649




N,M = map(int, input().split())


arr = [0]*M # len = M
is_used = [0]*N

# choose num for k'th element in arr
def func(k):
    # global arr, is_used

    # base condition
    if (k == M):
        print(' '.join(map(str, arr)))
        return
    
    # loop
    for i in range(N):
        if not is_used[i]:
            arr[k] = i+1
            is_used[i] = 1
            func(k+1)
            is_used[i] = 0

func(0)









