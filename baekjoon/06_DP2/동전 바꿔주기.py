# 2624

'''
푸는데 한 4시간은 걸린거 같다.
완전탐색으로 푸는데 시간초과 됐다.(코멘트 처리된 부분)
풀이를 검색해서 배끼니까 이해가 됐다.

coin이 value가 같은게 2개 이상일수도 있음.. ㅎㅎ

<풀이>
dp,혹은 memoization풀이라고 하는데 잘 이해는 안된다.
그냥 coin 1개 써서 가능한 경우의수(모든 값에 대해), 2개써서 .., 3개 써서.. 이렇게 쌓아가는 풀이이다.
1. coin 을 내림차순으로 정리 (안해도 무관)
2. 한 coin에 대해, 
    가장 큰 값부터 내려가면 서 `dp[target] += sum(dp[target-x], dp[target-2*x], .., dp[target-c*x])` 를 해줌
    모든 값(T->0)까지 다 해주면 그 코인 + 전 코인들을 이용해 가능한 가짓수가 구해짐
3. 모든 coin에 대해 반복.
'''

import sys

T = int(input())
K = int(input())
p = [] # value
p2n = {} # p2n[value] = amount
for _ in range(K):
    a,b = map(int, sys.stdin.readline().split())
    p.append((a,b))
p.sort(reverse=True)

dp = [0]*(T+1) # dp[x] = # of ways to make x
dp[0] = 1
for x,count in p:
    target = T
    while target >= 0:
        i = 0
        for j in range(1,count+1): # dp[target] += sum(dp[target-x], dp[target-2*x], .., dp[target-c*x])
            prev = target-j*x
            if prev < 0: break
            dp[target] += dp[prev]
        target -= 1
print(dp[T])














# baseline = [0]*K # minimum cost for each level entered
# baseline[-1] = T - p[-1]*p2n[p[-1]]
# for i in range(K-2,0,-1):
#     baseline[i] = baseline[i+1] - p[-i]*p2n[p[-i]]
# print(baseline)



# stack = [] # [([a,b,c,..],cost), ] amount for each coin
# max_p = p[0]
# for i in range(p2n[max_p]+1):
#     stack.append(([i],i*max_p))

# total = 0
# while stack:
#     cur,base_cost = stack.pop()
#     level = len(cur)

#     if base_cost < baseline[level-1]:
#         continue
#     print(cur)
#     if base_cost == T:
#         total += 1
#         continue
#     if level == K:
#         continue

#     for i in range(p2n[p[level]]+1):
#         cost = base_cost + i*p[level]
#         if cost > T:
#             break
#         stack.append((cur+[i],cost))
# print(total)
















