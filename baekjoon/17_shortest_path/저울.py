# 10159

from collections import defaultdict

N = int(input())
M = int(input())

pos_flow = defaultdict(list)
neg_flow = defaultdict(list)
for _ in range(M):
    a,b = map(int, input().split())
    pos_flow[b].append(a)
    neg_flow[a].append(b)
    

ans = []
for n in range(1, N+1):
    negs = neg_flow[n][:]
    poss = pos_flow[n][:]
    neg_visited = [0]*(N+1)
    pos_visited = [0]*(N+1)
    for nn in negs:
        neg_visited[nn] = 1
    for pp in poss:
        pos_visited[pp] = 1
    while negs:
        cur = negs.pop()
        for nn in neg_flow[cur]:
            if neg_visited[nn] == 0:
                neg_visited[nn] = 1
                negs.append(nn)
    while poss:
        cur = poss.pop()
        for nn in pos_flow[cur]:
            if pos_visited[nn] == 0:
                pos_visited[nn] = 1
                poss.append(nn)
    
    # print('n',n)
    # print('nl', neg_visited)
    # print('pl', pos_visited)
    # print('------------------')
    ans.append(N-1-sum(neg_visited)-sum(pos_visited))

for aa in ans:
    print(aa)
