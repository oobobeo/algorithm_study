# 9465

'''
쉬운 dp
'''

import sys

T = int(input())
for _ in range(T):
    n = int(input())
    sticker = [list(map(int, sys.stdin.readline().split())), list(map(int, sys.stdin.readline().split()))]
    
    ans = [sticker[0][0], sticker[1][0], 0]
    for i in range(1,n):
        a0 = max(ans[1]+sticker[0][i], ans[2]+sticker[0][i])
        a1 = max(ans[0]+sticker[1][i], ans[2]+sticker[1][i])
        a2 = max(ans)
        ans = [a0,a1,a2]
    print(max(ans))

