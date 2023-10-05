# 15654

N,M = map(int, input().split())
arr = list(map(int, input().split()))

is_used = [0]*N
ans = []

def prop(cur, count):
    if count == 1:
        for i in range(N):
            if is_used[i] == 0:
                ans.append(cur+[arr[i]])
        return
    count -= 1
    for i in range(N):
        if is_used[i] == 0:
            is_used[i] = 1
            prop(cur+[arr[i]], count)
            is_used[i] = 0
            

prop([], M)
for x in sorted(ans):
    print(*x)
