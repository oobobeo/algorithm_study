# 18185

# Ai = 3
# Ai + Ai+1 = 5
# Ai + Ai+1 + Ai+2 = 7

# 그리디로 
# 3개 연속인것 최대로 ㅆ고
# 2개 연속인것 최대로 쓰고
# 1개 연속인것 최대로 쓰면 됨.

# 가장 숫자 큰것부터.
# 12121 같이 같은 숫자가 2칸이하로 띄어져 있으면 동시에 포함해야됨.
# -> 3기둥 합이 가장 큰것부터 하면 되는거 같음.


import sys
import functools

N = int(input())

arr = list(map(int, sys.stdin.readline().split()))
abc = [[0]*3 for _ in range(N)] # abc[i][a,b,c]

result = 0

# A = 3
# B = 5
# C = 7

''' 
1.  i-1번 공장의 “A가 적힌 라면”을 최대한 많이 이용하여,
    i번 공장의 라면에 B를 적는다.
2.  i-1번 공장의 “B가 적힌 라면”을 최대한 많이 이용하여, 
    i번 공장의 라면에 C를 적는다.
3.  남은 i번 공장의 라면에 B를 적는다
'''
# a | ab | abc 이런식으로 track함.
# a: cost 3
# b: cost 2
# c: cost 2
abc[0] = [arr[0],0,0]
for i in range(1,N):
    pa, pb, _ = abc[i-1]
    curr = arr[i]
    # a->b
    if curr <= pa: # set all to b
        abc[i][1] = curr
        continue
    abc[i][1] = pa
    curr -= pa
    # b->c
    if curr <= pb: # set all to c
        abc[i][2] = curr
        continue
    abc[i][2] = pb
    curr -= pb
    # rest to a
    abc[i][0] = curr

result = 0
for i in range(N):
    result += abc[i][0]*3
    result += abc[i][1]*2
    result += abc[i][2]*2

print(result)