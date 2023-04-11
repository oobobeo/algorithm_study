# 4256



'''
tree문제들이 그렇듯, 실제 tree를 구현해서 생각하지 않고,
분할정복을 사용했다.

inorder: l[] -> n   -> r[]
post   : l[] -> r[] -> n
pre    : n   -> l[] -> r[]
재귀적으로 각 l,n,r들에 대해 처리해 주면 된다.
l,n,r은 각각 같은 트리를 나타내고 있다는점 파악( node의 순서만 다르지 내용물은 같음 )


N <= 10**6 인데 recursionlimit 10**6으로 하면 메모리초과되고, 10**5로 하면 잘 통과된다.
timelimit: 5s 인데 13초로 도는데 통과됐다.
'''


import sys

sys.setrecursionlimit(10**3)


def find_pst(x,y, a,b, c,d):
    global ino, pst, pre
    # ino [x:y]
    # pst [a:b]
    # pre [c:d]
    root_val = pre[c]
    ino_root = None
    for i in range(y-x+1):
        if ino[x+i] == root_val:
            ino_root = x+i
            break

    l_len = ino_root - x
    r_len = y - ino_root
    # root
    pst[b] = root_val
    # left
    if l_len:
        find_pst(x,ino_root-1, a,a+l_len-1, c+1,c+l_len)
    # right
    if r_len:
        find_pst(ino_root+1,y, a+l_len,b-1, d-r_len+1,d)


T = int(input())
for _ in range(T):
    N = int(input())
    pre = sys.stdin.readline().split()
    ino = sys.stdin.readline().split()
    pst = ['0']*N
    find_pst(0,N-1,0,N-1,0,N-1)
    print(*pst)
