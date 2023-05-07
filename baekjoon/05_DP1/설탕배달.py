# 2839

'''
5가 최대한 많아야 전체 봉투수가 적어진다.
5를 최대치로 잡고 1씩 줄이면서 greedy하게 끼워 맞춰주기
'''

import sys

N = int(input())

if N == 4:
    print(-1)
    exit(0)

threes = 0
fives = N//5
if fives*5 < N:
    fives += 1
while fives >= 0:
    if threes*3+fives*5 == N:
        print(threes + fives)
        exit(0)
    if threes*3+fives*5 > N:
        fives -= 1
        while threes*3+fives*5 < N:
            threes += 1
print(-1)
