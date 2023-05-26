# 7453

'''
defaultdict 은 timeout 난다.
`dict[k] = dict.get(k, 0) + 1` 를 사용하자!!

2_pointer로도 풀수 있나보다
'''
# O(n^2 * 1), n=4000. 16_000_000

from collections import defaultdict

N = int(input())
A,B,C,D = [],[],[],[]
for _ in range(N):
    a,b,c,d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
# A = sorted(set(A))
# B = sorted(set(B))
# C = sorted(set(C))
# D = sorted(set(D))

# A + [B + (C+D)]
# B:  1 2 3 4 5
# C': 6 7 8 9 10

A_B = []
for i in range(len(A)):
    for j in range(len(B)):
        A_B.append(A[i]+B[j])

# C_D = defaultdict(int)
C_D = {}
for i in range(len(C)):
    for j in range(len(D)):
        C_D[C[i]+D[j]] = C_D.get(C[i]+D[j], 0) + 1

count = 0
for a in A_B:
    count += C_D.get(-a, 0)

print(count)
