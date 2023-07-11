from collections import defaultdict
def solution(N, edges):
    answer = 0
    adj = defaultdict(list)
    for a,b in edges:
        adj[a].append(b)
        adj[b].append(a)
    
    def dfs(n):
        stack = [n]
        vis = [0]*(N+1)
        vis[n] = 1
        d = [0]*(N+1)
        while stack:
            cur = stack.pop()
            vis[cur] = 1
            for nei in adj[cur]:
                if vis[nei]: continue
                vis[nei] = 1
                stack.append(nei)
                d[nei] = d[cur] + 1
        max_d = max(d)
        ret = []
        for i,x in enumerate(d):
            if x == max_d:
                ret.append(i)
        return ret,max_d
    
    dn1,_ = dfs(1)
    # print(dn1,_)
    dn2s, max_dist = dfs(dn1[0])
    if len(dn2s) > 1:
        return max_dist
    else: # 1개
        dn3s, max_dist = dfs(dn2s[0])
        if len(dn3s) > 1:
            return max_dist
        else:
            return max_dist -1
        