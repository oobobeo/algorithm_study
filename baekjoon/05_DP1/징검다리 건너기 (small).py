# 22869


'''
N = 5000
O(N^2)으로 푼다
'''

N,K = map(int, input().split())
stone = list(map(int, input().split()))

reachable = [0]*N
reachable[0] = 1
for i in range(1,N):
    for j in range(i):
        if reachable[j] and (i-j)*(1+abs(stone[i]-stone[j])) <= K:
            reachable[i] = 1
            break
if reachable[-1]:
    print("YES")
else:
    print("NO")
