# 8980

'''
(end-st,st) 기준으로 졍렬했다가 틀림.
정답보고 (end) 기준으로 정렬하는게 답인걸 알게됨.
빨리 내려놔야 끝부분이 뒤에있는 택배를 들수 있는 경우수가 많아진다.
end 순으로 정렬하면, 어차피 뒤에 있는 (st,en,택배수) pair는 앞에 처리한 pair에 걸린다.(혹은 아예 상관이 없거나.)
'''

import sys

N,C = map(int, input().split())
task = []
for _ in range(int(input())):
    a,b,c = map(int, sys.stdin.readline().split())
    task.append([b,a,b,c])
task.sort(reverse=True)

total_weight = 0
space = [C]*(N)
while task:
    _,a,b,c = task.pop()
    max_possible_weight = space[a]
    for i in range(a+1,b):
        max_possible_weight = min(max_possible_weight,space[i])
    max_possible_weight = min(max_possible_weight,c)
    if max_possible_weight > 0:
        for i in range(a,b):
            space[i] -= max_possible_weight
        total_weight += max_possible_weight
    # print(a,b,c,space)

print(total_weight)









