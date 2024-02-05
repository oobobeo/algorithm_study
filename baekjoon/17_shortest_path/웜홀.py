# 1865

'''
두개 이상의 끊어진 sub-graph로 나뉘어져 있는 상황을 고려해야했다.

'''

F = int(input())
ans = []
for _ in range(F):
    N,M,W = map(int, input().split())
    
    edges = []
    for _ in range(M):
        a,b,d = tuple(map(int, input().split()))
        edges.append((a,b,d))
        edges.append((b,a,d))
    
    for _ in range(W):
        a,b,d = tuple(map(int, input().split()))
        edges.append((a,b,-d))

    dists = [float("inf")]*(N+1)
    dists[0] = 0
    # find neg cycle using Bellman Ford alg
    # for sub_graph
    flag = 0
    while float("inf") in dists:
        dists[dists.index(float("inf"))] = 0 # arbitrary start
        for i in range(N):
            for s,d,w in edges:
                if dists[s] != float("inf") and dists[d] > dists[s] + w:
                    if i == N-1:
                        flag = 1
                        break
                    dists[d] = dists[s] + w
        if flag: break
    ans.append(flag)

for aa in ans:
    if aa == 0:
        print("NO")
    elif aa == 1:
        print("YES")

