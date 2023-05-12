# 10942

'''
아이디어 처음 생각해 내는것이 살짝 까다로웠음
'''

import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))

# dp init
palin = [[False]*N for _ in range(N)]
for i in range(N):
    palin[i][i] = True
    if i+1 <= N-1:
        palin[i][i+1] = (arr[i] == arr[i+1])

# dp
for i in range(2,N):
    for j in range(N-i):
        # cur = j,i+j
        # print(j,i+j,'|',i+1,i+j-1,'|',)
        palin[j][i+j] = palin[j+1][i+j-1] and arr[j] == arr[i+j]


M = int(input())
for _ in range(M):
    s,e = map(int, sys.stdin.readline().split())
    if palin[s-1][e-1]:
        print(1)
    else:
        print(0)










