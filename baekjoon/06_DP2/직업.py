# 2056

'''
질문 게시판에서 corner case 힌트를 얻었다.
문제 설명을 읽어보고 이상한 부분, edge case에 대한 예제로 testing을 하자!

--
ex)
 작업들 중에는, 그것에 대해 선행 관계에 있는 작업이
 하나도 없는 작업이 반드시 하나 이상 존재한다. (1번 작업이 항상 그러하다)
 -> 선행 관계가 없는 직업 여러개 있는 경우에
    max() 함수에서 "Value Error"가 났었음.
'''

import sys

N = int(input())

# dp[job] = accumulative time it took for the job
dp = [0]*(N+1)
jobs = {}
for i in range(1,N+1):
    arr = list(map(int, sys.stdin.readline().split()))
    jobs[i] = set(arr[2:])
    dp[i] = arr[0]
jobs[1] = set([0])
visited = set([0])

print(jobs)

while len(visited) < N+1:
    for j,pre in jobs.items():
        if j in visited: continue
        if pre.issubset(visited):
            dp[j] = max([dp[x] for x in pre] + [0]) + dp[j] # pre 가 empty set 일 수 도 있음!
            visited.update([j])

print(max(dp))
