# 1182
# two pointer이지만 backtracking 연습

import sys
sys.setrecursionlimit(1024*200)

N,S = map(int, input().split())
arr = [0] + list(map(int, sys.stdin.readline().split()))

# edge1: [0]+[0] 꼴들

# is_used = [0]*(N+1)
# is_used[0] = 1
ans = 0

# dfs but only goes up in idx
def dfs(idx, cur):
    global ans
    if cur == S:
        print(idx, cur)
        ans += 1
    # if idx == N:
    #     return
    for i in range(idx+1, N+1):
        dfs(i, cur+arr[i])

dfs(0,0)

# S가 0일 때만 정답처리 되버림!!
# 기존 arr 조작할 때는 알고리즘에서 edge case가 추가로 생긴다!
if S == 0:
    print(ans-1)
else:
    print(ans)




