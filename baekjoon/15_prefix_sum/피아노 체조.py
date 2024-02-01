# 21318

N = int(input())

l = [0]+list(map(int, input().split()))
Q = int(input())
qs = []
for q in range(Q):
    qs.append(list(map(int, input().split())))

arr = [0]*(N+1)

for i in range(1,N):
    if l[i] > l[i+1]:
        arr[i] = arr[i-1]+1
    else:
        arr[i] = arr[i-1]
arr[-1] = arr[-2]

for s,e in qs:
    print(arr[e-1]-arr[s-1])

print(arr)





