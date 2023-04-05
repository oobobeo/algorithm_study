# 1068


'''
일단 leaf node가 될 가능성이 있는 노드들을 leaf_cand에 넣어줄 것이다.
가능성있는 노드:
    1. 현재 leaf인 노드
    2. del_node의 parent (그 parent의 child가 del_node로 유일한 경우만)
loop:
    leaf_cand 의 노드에 대해 하나씩 위로 올라가면서 root나 del_node에서 멈추도록 했다.
    root에서 멈추는 경우만 leaf node로 인정해 주었다.

BFS,DFS로도 가능할듯.
'''


import sys


N = int(input())
parent = list(map(int, input().split()))
del_node = int(input())

# leaf candidates
parents = set(parent)
# parents.add(del_node)
leaf_cand = [x for x in range(N) if x not in parents]

child_num = 0
for i in range(N):
    if parent[i] == parent[del_node]: 
        child_num += 1
if parent[del_node] != -1 and child_num == 1: # root
    leaf_cand.append(parent[del_node])
# print(leaf_cand)

# check for each leaf candidates after deleting del_node
result = 0
for n in leaf_cand:
    while n != del_node and n != -1:
        n = parent[n]
    if n == -1:
        result += 1
        
print(result)
