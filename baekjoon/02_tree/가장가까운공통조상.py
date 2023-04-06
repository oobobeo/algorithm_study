# 3584




'''
<풀이>
parent[n] = p 테이블 만듦
node a,b 에 대해 각각
[a, .., root], [b, .., root] 구함.
list 동시 pop하면서 처음 달라지는 부분 구함
'''




import sys



T = int(input())
for _ in range(T):
    N = int(input())
    
    # setup parent[]
    parent = [0]*(N+1)
    # node1, node2 = map(int, sys.stdin.readline().split())
    # parent[node2] = node1
    for __ in range(N-1):
        a,b = map(int, sys.stdin.readline().split())
        parent[b] = a

    # get routes up to root
    node1, node2 = map(int, sys.stdin.readline().split())
    r1 = [node1]
    r2 = [node2]
    while True:
        node1 = parent[node1]
        if node1 == 0:
            break
        r1.append(node1)
    while True:
        node2 = parent[node2]
        if node2 == 0:
            break
        r2.append(node2)

    # compare routes
    cur = r1[-1]
    while r1 and r2:
        a = r1.pop()
        b = r2.pop()
        if a != b:
            break
        cur = a
    print(cur)



