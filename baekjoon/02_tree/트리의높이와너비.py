# 2250

'''
<풀이>
c[n] = (l,r)
lr[n] = (l_subtree_len, r_subtree_len)
pos[n] = idx
lv[l] = [idx's]

1. from input, make c[] -> find root
2. BFS: make lr[]
    BFS를 사용하고, rev_stack에 cur_node를 넣어주면,
    rev_stack.pop()을 해주었을때 child의 lr이 이미 계산된 것이 보장된다. (leaf -> root 방향 보장)
3. DFS: make pos[], lv[]
    root를 pos 0 으로 놓고, root부터 child들의 pos를 상대적으로 계산해준다.
4. calculate length for each lv.

<정해>
inorder[l -> n -> r] sort를 사용하면,
tree를 짜부시키는 것과 동일하므로, 문제의 idx순으로 순회하는 꼴이된다..


푸는데 1:30 좀 넘게 걸렸는데,
트리는 inorder,postorder,preorder 사용하는 방법 부터 생각하자!!!!!
'''

import sys
from collections import deque

N = int(input())


# 1. from input, make p[], c[] -> find root
c = [None]*(N+1)
root = set([x for x in range(1,N+1)])
for i in range(N):
    n,l,r = map(int, sys.stdin.readline().split())
    c[n] = (l,r)
    root.discard(l)
    root.discard(r)
# find root
root = root.pop()


# 2. BFS: make lr[]
lr = [[-1,-1] for _ in range(N+1)]
rev_stack = [] # to calcucate lr: leaf -> root, except for root
q = deque([root])
while q:
    cur = q.popleft()
    lc,rc = c[cur]
    # leaf
    if (lc,rc) == (-1,-1):
        lr[cur] = [0,0]
        # rev_stack.append(cur)
        continue
    # print(cur,lc,rc,lr[cur])
    if lc == -1:
        lr[cur][0] = 0
    if rc == -1:
        lr[cur][1] = 0
    # else
    if lc != -1:
        q.append(lc)
    if rc != -1:
        q.append(rc)
    rev_stack.append(cur)
while rev_stack:
    cur = rev_stack.pop()
    ll,rl = lr[cur]
    if ll == -1:
        lr[cur][0] = sum(lr[c[cur][0]]) + 1
    if rl == -1:
        lr[cur][1] = sum(lr[c[cur][1]]) + 1

# 3. DFS: make pos[], lv[]
pos = [0]*(N+1) # pos[root] = 0
lv = [[] for _ in range(N+1)] # idx's
stack = [(root,1)] # (node,level)
while stack:
    cur,level = stack.pop()
    l,r = c[cur]
    if l != -1:
        stack.append((l,level+1))
        pos[l] = pos[cur]-lr[l][1]-1
        lv[level+1].append(pos[l])
    if r != -1:
        stack.append((r,level+1))
        pos[r] = pos[cur]+lr[r][0]+1
        lv[level+1].append(pos[r])


# 4. calculate result
result = [1,1]
for i in range(1,len(lv)):
    sorted_lv = sorted(lv[i])
    if not sorted_lv: continue
    length = sorted_lv[-1] - sorted_lv[0] + 1
    if length > result[1]:
        result = [i, length]

print(*result)
