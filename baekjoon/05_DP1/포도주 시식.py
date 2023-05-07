# 2156

'''
n까지 봤을떄 최대로 먹을 수 있는 양을 case 분류[??x,?xo,xoo] 로 분류해서
n+1까지 봤을떄의 값의 확답을 얻을수 있게 함
'''


n = int(input())
ans = [0,int(input()),0]
for _ in range(1,n):
    cur = int(input())
    a0 = max(ans)
    a1 = ans[0]+cur
    a2 = ans[1]+cur
    ans = [a0,a1,a2]
print(max(ans))





