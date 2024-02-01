# 20438

'''
edge1) 처음에 코드를 받는 학생이 조는 학생인 경우를 놓쳤다.

'''


N,K,Q,M = map(int, input().split())

sleep = list(map(int, input().split()))
start = list(map(int, input().split()))

interval = []
for _ in range(M):
    interval.append(list(map(int, input().split())))

stu = [0]*(N+3)
for s in sleep:
    stu[s] = -1

for s in start:
    i = 1
    if stu[s] == -1: continue
    while s*i <= N+2:
        if stu[s*i] != -1:
            stu[s*i] = 1
        i += 1
    # print(s,stu)

acc_sum = [0]*(N+3)
for i in range(1,N+3):
    if stu[i] == 0 or stu[i] == -1:
        acc_sum[i] = acc_sum[i-1]
    elif stu[i] == 1:
        acc_sum[i] = acc_sum[i-1] + 1

for s,e in interval:
    print(e-s+1 - acc_sum[e] + acc_sum[s-1])

# print(acc_sum)
