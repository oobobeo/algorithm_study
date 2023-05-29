# 22860

'''
문제가 조건이 명확하지 않은 부분이 있었다.
'''

from collections import defaultdict, deque

parent = {} # parent[child] = parent; folder only
child = defaultdict(list) # child[parent] = [children]
files = defaultdict(list) # files[folder] = [all files]
q = deque()

N,M = map(int, input().split())
# cmd = defaultdict(list)
for _ in range(N+M):
    p,f,c = input().split() # c=1: folder, c=0: file
    if c == '1':
        child[p].append(c)
        parent[f] = p
    else:
        q.append((p,f,c))

visited = set() # folders

# BFS main
while q:
    p,f,c = q.popleft()
        
    while p != "main":
        files[p].append(f)
        p = parent[p]
    files[p].append(f)
        
        
Q = int(input())
result = []
for _ in range(Q):
    query = input().split('/')
    f = query[-1]
    
    result.append((len(set(files[f])), len(files[f])))
    
for r in result:
    print(*r)
