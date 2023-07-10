from collections import defaultdict, deque
def solution(n, path, order):
    answer = True
    vis = [0]*n
    vis[0] = 1
    adj = defaultdict(list)
    for a,b in path:
        adj[a].append(b)
        adj[b].append(a)
    req = defaultdict(set)
    rev_req = defaultdict(set)
    for a,b in order:
        req[b].add(a)
        rev_req[a].add(b)
        
    if 0 in req.keys():
        return False
    
    # vis[], adj{}, req{}
    q = deque(adj[0]) # edges
    edges = [0]*n
    edges[0] = 1
    for ee in adj[0]:
        edges[ee] = 1
    counter = 0
    while q:
        cur = q.popleft()
        if vis[cur]: continue
        
        fullfilled = True
        ll = list(req[cur])
        for r in ll:
            if vis[r] == 0:
                fullfilled = False
                break
            else:
                req[cur].discard(r)
                rev_req[r].discard(cur)
                
        if fullfilled:
            counter = 0
            vis[cur] = 1
            edges[cur] = 0
            for nxt in adj[cur]:
                if vis[nxt] == 0: # and edges[nxt] == 0:
                    q.appendleft(nxt)
                    edges[nxt] = 1
            for nxt in rev_req[cur]:
                if len(req[nxt]) == 1 and edges[nxt]:
                    q.appendleft(nxt)
            
                
        else: # x fullfilled
            q.append(cur)
            counter += 1
            
        if counter > len(q):
        # if counter > len(q)+10:
            break
    if min(vis) == 1:
        return True
    else:
        return False
        