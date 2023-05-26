# 22858

import sys


N,K = map(int, input().split())

S = list(map(int, sys.stdin.readline().split()))
D = list(map(int, sys.stdin.readline().split()))


for _ in range(K):
    P = ['']*N
    for d,s in zip(D,S):
        P[d-1] = s
    S = P[:]
    
    
print(*P)
