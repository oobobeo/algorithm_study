# 5639







import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.l = None
        self.r = None
        self.p = None

root = None
cur = root
while line := sys.stdin.readline():
    val = int(line)
    n = Node(val)
    if not root:
        root = cur = n
        continue
    while True:
        if val < cur.val:
            if not cur.l:
                cur.l = n
                n.p = cur
                cur = n
                break
            else:
                cur = cur.l
                continue
        else: # cur.val < val
            if not cur.r:
                cur.r = n
                n.p = cur
                cur = n
                break
            else:
                cur = cur.r
                continue


