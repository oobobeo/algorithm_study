# 15649

import sys
import itertools

N,M = map(int, input().split())

a = list(itertools.permutations([i+1 for i in range(N)], r=M))
# if M > 1:
#     b = list(itertools.combinations(reversed([i+1 for i in range(N)]), r=M))
# else:
#     b = []
# a = a + b
# a.sort()
for x in a:
    print(*x)








