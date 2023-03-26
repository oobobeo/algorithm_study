



















# 1991


import sys

class Node():
    def __init__(self, val, l, r):
        self.val = val
        self.l = l
        self.r = r
node = {}
for alpha in 'ABCDEFGHIJKLMNOPQRSTUVWZYX':
    node[alpha] = Node(alpha,None,None)


N = int(input())
for _ in range(N):
    n,l,r = sys.stdin.readline().split()
    if l != '.':
        node[n].l = node[l]
    if r != '.':
        node[n].r = node[r]

# pre
pre_list = []
def pre(n):
    if n == None: return
    pre_list.append(n.val)
    pre(n.l)
    pre(n.r)

# mid
mid_list = []
def mid(n):
    if n == None: return
    mid(n.l)
    mid_list.append(n.val)
    mid(n.r)

# post
post_list = []
def post(n):
    if n == None: return
    post(n.l)
    post(n.r)
    post_list.append(n.val)


pre(node['A'])
mid(node['A'])
post(node['A'])

print(''.join(pre_list))
print(''.join(mid_list))
print(''.join(post_list))