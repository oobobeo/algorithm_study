# 1647

'''
나누고 MST 구하는거는 너무 경우수가 많다.
MST구하고 1번 나누는거는 쉬운데 최적해가 아닐 가능성이 높다.
-> 2개로 나누었을 떄 각 노드들이 연결된 형태가 최적이면, 해당 상황이 최적해이다.
    -> kruskal 알고리즘상, edge sort하고 작은것부터 연결하기 떄문에 최적해이다.
        (kruskal alg의 근거는 생략)
'''

import sys
from collections import defaultdict

N,M = map(int, input().split())

edges = []
for _ in range(M):
    a,b,c = map(int, sys.stdin.readline().split())
    edges.append((c,a,b))

parent  = [i for i in range(N+1)]
rank    = [0]*(N+1)
def find(x):
    if parent[x] == x:
        return x
    y = find(parent[x])
    parent[x] = y
    return y

def union(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return True
    else:
        if rank[x] > rank[y]:
            parent[y] = x
        elif rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] == rank[y]:
            parent[x] = y
            rank[x] += 1
        return False

# kruskal's alg
edges.sort()
tree = []
for cost, x, y in edges:
    if union(x,y): continue
    else:
        tree.append(cost)
    if len(tree) == N-1: break

print(sum(tree) - max(tree))
