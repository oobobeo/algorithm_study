# 20291


d = {}
l = []
N = int(input())
for _ in range(N):
    _, ext = input().split('.')
    
    l.append(ext)
    d[ext] = d.get(ext,0) + 1
l = sorted(set(l))
for k in l:
    print(k,d[k])


