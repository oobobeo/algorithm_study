# 21914

'''
엄청 오래걸림.
edge case는 특별한 경우를 생각해서 찾아낼 수 있었다.
edge1) 같은문자열, 다른점수 쌍
edge2) 글자 1개
edge3) 문자열 길이 = 1

<sol>
dp[i][j] = i~j 구간에서의 최대값.
1. matches[s][]: s의 각 idx에서 그 idx가 끝인 (offset,score) pair들을 넣어준다.
2. matches[s][]를 가지고 dp[k][k]를 max(matches[k]+[1]) 로 init해준다.
3. [0,1]->[-2,-1] 같이 대각선으로 dp[i][j]를 채워줌.
4. 구간이 전체인 dp[0][s-1]이 정답.

<찾은 해답>
dp[i] = 0~i-1 구간에서 최대값.
dp[i+1] = max(dp[i], [dp[i-k1]+x1, dp[i-k2]+x2, ..])
'''

'''
dp[] arr를 1차원이 되는지 먼저 확인해보고 안되면 2차원을 고려하자..
'''


import sys

S = list(input())
s = len(S)
M = int(input())
ax = []
for _ in range(M):
    a,x = sys.stdin.readline().split()
    ax.append((a,int(x)))



def match(i,a):
    if len(a) > i+1: return False
    for j in range(1,len(a)+1):
        if a[-j] != S[i-j+1]: return False
    return True

# matches init
matches = [[] for _ in range(s)]
for a,x in ax:
    for i in range(s):
        if match(i,a):
            matches[i].append((-len(a)+1,x))



# dp init
dp = [[1]*s for _ in range(s)]
for i in range(s):
    single = [x[1] for x in matches[i] if x[0] == 0]
    dp[i][i] = max(single + [1])

# dp
for i in range(1,s):
    for j in range(s-i):
        # cur = j,i+j | 0,i -> i,0
        scores = [dp[j][i+j-1]+1] # (abcd + 1)
        for offset,score in matches[i+j]:
            if i+j+offset < j: continue
            elif i+j+offset == j: # exact match
                scores.append(score)
            else:
                scores.append(score + dp[j][i+j+offset-1])
        dp[j][i+j] = max(scores)

print(dp[0][s-1])


