# backtracking으로 풀어보자

N,M = map(int, input().split())

hist = []
ans = []
def nxt(hist, count):
    if count == 1:
        for i in range(N):
            ans.append(hist+[i+1])
        return
    count -= 1
    for i in range(N):
        nxt(hist+[i+1], count)

nxt(hist, M)
for x in ans:
    print(*x)
