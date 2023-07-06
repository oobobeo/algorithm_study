from collections import defaultdict
def solution(info, edges):
    c = defaultdict(set) # c[parent] = [children]
    for parent, child in edges:
        c[parent].add(child)
    
    global max_s
    max_s = 1
    def search(s,w,edges):
        global max_s
        if s <= w:
            return
        
        for e in edges:
            new_edges = edges.copy()
            new_edges.discard(e)
            new_edges |= c[e]
            if info[e] == 0: # edge = sheep
                max_s = max(max_s, s+1)
                if new_edges and s+1 > w:
                    search(s+1, w, new_edges)
            else: # edge = wolf
                if new_edges and s > w+1:
                    search(s, w+1, new_edges)
                
    
    search(1,0, c[0])
    print(max_s)
    return max_s
    
    
    
    
    
    
    
    
#     from itertools import combinations
#     from collections import defaultdict, deque
#     adj = defaultdict(list)
#     p = defaultdict(int) # p[child] = parent
#     c = defaultdict(list) # c[parent] = child
#     for a,b in edges:
#         adj[a].append(b)
#         adj[b].append(a)
#         p[b] = a
#         c[a].append(b)
    
#     '''
#     완전탐색
#     1. combinations -> 무조건 방문한 sheep node idx들 집합에 대해
#         1-1. validate
#         1-2. 가능하면, update result
#     '''
#     sheeps = [] # sheep node num, excluding 0
#     wolfs = []
#     for i in range(1, len(info)):
#         if info[i] == 0:
#             sheeps.append(i)
#         else:
#             wolfs.append(i)
    
#     # set, int, int
#     cand = []
#     def expand(conquered, w_count, s_count): # target = shallowest sheeps
#         edges = []
#         for node in conquered:
#             for child in c[node]:
#                 if child not in conquered:
#                     edges.append(child)
        
#         # search until all sheep encounters | leaf
#         routes = [] # ([wolves], [sheeps])
#         for e in edges:
#             stack = [[e]]
#             while stack:
#                 cur_route = stack.pop()
#                 cur = cur_route[-1]
                
#                 if len(c[cur]) == 1:
#                     if info[c[cur][0]] == 0: # sheep
#                         routes.append((cur_route, [c[cur][0]]))
#                     else: # wolf
#                         temp = cur_route[:]
#                         temp.append(c[cur][0])
#                         stack.append(temp)
#                 elif len(c[cur]) == 2:
#                     if info[c[cur][0]] == 0 and info[c[cur][1]] == 0: # sheep, sheep
#                         routes.append((cur_route, c[cur]))
#                     elif info[c[cur][0]] == 1 and info[c[cur][1]] == 0:
#                         temp = cur_route[:]
#                         temp.append(c[cur][0])
#                         stack.append(temp)
#                         routes.append((cur_route, [c[cur][1]]))
#                     elif info[c[cur][0]] == 0 and info[c[cur][1]] == 1:
#                         temp = cur_route[:]
#                         temp.append(c[cur][1])
#                         stack.append(temp)
#                         routes.append((cur_route, [c[cur][0]]))
#                     else: # wolf, wolf
#                         temp = cur_route[:]
#                         temp.append(c[cur][0])
#                         stack.append(temp)
#                         temp = cur_route[:]
#                         temp.append(c[cur][1])
#                         stack.append(temp)
                        
#         # dfs for each routes.
#         # find max sheep yield
#         # calculate reachability
#         # recursive call if reachable
#         for r,s in routes: # [wolfs], [sheeps]
#             # bfs
#             q = deque(s)
#             sheep_set = set(s)
#             while q:
#                 cur = q.popleft()
#                 if info[cur] == 0: # sheep
#                     sheep_set.add(cur)
#                     for child in c[cur]:
#                         if info[child] == 0:
#                             q.append(child)
#             # expand
#             if s_count > w_count + len(r):
#                 temp = conquered.union(set(r))
#                 temp = temp.union(sheep_set)
#                 expand(temp, w_count+len(r), s_count+len(sheep_set))
#             print(s_count, w_count,w_count + len(r), r,  conquered)
#         cand.append(s_count)
        
        
        
#     # init
#     q = deque([0])
#     sheep_set = set([0])
#     s_count = 0
#     while q:
#         cur = q.popleft()
#         if info[cur] == 0: # sheep
#             s_count += 1
#             sheep_set.add(cur)
#             for child in c[cur]:
#                 if info[child] == 0:
#                     q.append(child)
    
#     # expand
#     print(sheep_set)
#     expand(sheep_set,0,len(sheep_set))
    
#     cand.sort()
#     return cand[-1]
            
            
            
            
            
            
            
    