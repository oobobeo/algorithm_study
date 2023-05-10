# 1106

'''
동전바꿔주기(2624)랑 비슷한 문제
'''
# 도시,홍보비용,고객늘어나는수


G,N = map(int, input().split()) # G명, N도시
# G = goal

cn = [] # (cost, number)
for _ in range(N):
    c,n = map(int, input().split())
    cn.append((c,n))
cn.sort(reverse=True)

dp = [1000*100000]*(1101) # dp[number] = cost, cost 최소화
dp[0] = 0
for i in range(N):
    c,n = cn[i]
    for j in range(1,1101): # target = j
        offset = 1
        while j-offset*n >= 0:
            dp[j] = min(dp[j], dp[j-offset*n]+offset*c)
            offset += 1
    # print(dp)
print(min(dp[G:]))
