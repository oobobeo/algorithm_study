def solution(n, paths, gates, summits):
    from heapq import heappush, heappop
    from collections import defaultdict
    adj = defaultdict(list)
    for i,j,w in paths:
        adj[i].append((j,w))
        adj[j].append((i,w))
    summit_list = [0]*(n+1)
    gate_list = [0]*(n+1)
    for x in gates:
        gate_list[x] = 1
    for x in summits:
        summit_list[x] = 1
    
    # djikstra 변형
    h = [(g,0) for g in gates] # (node, inten)
    # answer = [float('inf'), float('inf')]
    inten = [float('inf')]*(n+1)
    while h:
        cur_node, cur_inten = heappop(h)
        if summit_list[cur_node]: continue
        for nxt_node, nxt_inten in adj[cur_node]:
            if max(cur_inten, nxt_inten) < inten[nxt_node]:
                inten[nxt_node] = max(cur_inten, nxt_inten)
                if summit_list[nxt_node]: continue
                heappush(h, (nxt_node, inten[nxt_node]))
    
    # print(inten)
    result = []
    for i,val in enumerate(inten):
        if summit_list[i]:
            result.append((i,val))
    result.sort(key=lambda x: (x[1],x[0]))
    return result[0]
    
    
    
    
    
    
    
    
    
    
    
    
    
    