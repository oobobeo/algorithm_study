# 2285

'''
처음엔 y = b|x-a| + b|x-a| + .. 꼴의 식의 argmin(x)를 구하려고
x를 bisect 비스무리하게 gradient descent마냥 구하려함.
사실 그냥 인구수 절반을 딱 넘어갈 떄 최소 였음..

'''


import sys

N = int(input())
dist = [0]*(N)
xa = [(0,0)]*(N)
total = 0
for i in range(N):
    x_, a_ = map(int,sys.stdin.readline().split())
    xa[i] = (x_,a_)
    total += a_
xa.sort()

def d(i):
    dist = 0
    for j in range(0,i):
        dist += (xa[i][0]-xa[j][0])*xa[j][1]
    for j in range(i+1,N):
        dist += (-xa[i][0]+xa[j][0])*xa[j][1]
    return dist

count = 0
for i in range(N):
    x,a = xa[i]
    count += a
    if count >= (total+1) // 2:
        print(x)
        exit(0)

