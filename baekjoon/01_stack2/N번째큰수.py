# 2075
# input -> sys.stdin.readline().strip()

import sys

n = int(input())

lists = [] # [[..], ..]
for i in range(n):
    # lists.append( list(map(int, sys.stdin.readline().strip().split())) )
    lists += list(map(int, sys.stdin.readline().strip().split()))
    lists = sorted(lists)[-n:]

# lists = [elem for sublist in lists for elem in sublist]


# print(total_lists)

# lists = sorted(lists)

print(lists[-n])



