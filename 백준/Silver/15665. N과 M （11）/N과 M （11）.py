# 15665

N,M = map(int, input().split())
arr = list(map(int, input().split()))

is_used = [0]*N
ans = []

def prop(cur, count):
    if count == 1:
        for i in range(N):
            ans.append(cur+[arr[i]])
        return
    count -= 1
    for i in range(N):
        prop(cur+[arr[i]], count)
            

prop([], M)
ans.sort()
ans2 = set([' '.join(map(str,x)) for x in ans])
ans = [list(map(int, x.split())) for x in ans2]


for x in sorted(ans):
    print(*x)
