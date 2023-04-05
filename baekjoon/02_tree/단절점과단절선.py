# 14675


'''
해당 정점이 단절점이려면, 그 정점의 adjacent 정점이 2개 이상이 여야한다.
모든 간선은 단절선이다.
한 정점에 대해 adj 개수를 O(1)에 알고 싶으므로, adj{[]}를 사용했다.

처음에 edge정보도 필요한줄 알았는데 아니였다
'''






import sys
from collections import defaultdict

adj = defaultdict(list)  # adj[n] = [..]
edge = [] # [(a,b), ..]

N = int(input())

for _ in range(N-1):
    a,b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

Q = int(input())
# t:1 k정점 단절점, t:2 k간선 단절선
for _ in range(Q):
    t,k = map(int, sys.stdin.readline().split())
    if t == 1:
        if len(adj[k]) >=2:
            print('yes')
        else:
            print('no')
    else: # t == 2
        print('yes')

