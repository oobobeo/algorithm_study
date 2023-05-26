# 10994

N = int(input())
arr = [[' ']*(1+(N-1)*4) for _ in range(1+(N-1)*4)]
n = (1+(N-1)*4)

for i in range(n):
    if i <= n//2 - 1:
        if i % 2 == 0:
            arr[i] = ['*']*n
            for j in range(1, i//2+1):
                arr[i][j*2-1] = arr[i][n-j*2] = ' '
        else: # i % 2 == 1
            for j in range(0, i//2+1):
                arr[i][j*2] = arr[i][n-1-j*2] = '*'
                
    elif i >= n//2 + 1:
        if i % 2 == 0:
            arr[i] = ['*']*n
            for j in range(1, (n-i)//2+1):
                arr[i][j*2-1] = arr[i][n-j*2] = ' '
        else: # i % 2 == 1
            for j in range(0, (n-i)//2):
                arr[i][j*2] = arr[i][n-1-j*2] = '*'
      
    else: # middle
        for j in range(n//2 + 1):
            arr[i][j*2] = '*'

for l in arr:
    print(*l, sep='')
    