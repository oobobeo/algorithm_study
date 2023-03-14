# 9663




N = int(input())

# cloumn
is_used1 = [0]*N
# diag1: x+y = 0~2N-2
is_used2 = [0]*(2*N-1)
# diag2: x-y+N-1 = 0~2N-2
is_used3 = [0]*(2*N-1)


count = 0
# for k'th row
def func(k):
    global count
    # base condition
    if k == N:
        count += 1
        return
    
    # loop
    for x in range(N):
        if not is_used1[x] and not is_used2[x+k] and not is_used3[x-k+N-1]:
            is_used1[x] = 1
            is_used2[x+k] = 1
            is_used3[x-k+N-1] = 1
            func(k+1)
            is_used1[x] = 0
            is_used2[x+k] = 0
            is_used3[x-k+N-1] = 0

func(0)
print(count)

