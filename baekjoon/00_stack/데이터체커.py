
# 22942


# s[]: 원과 x축과의 접점에 해당하는 칸에 원의 다른점 접점좌표 넣기
# 현재 원의 x-r ~ x+r 넣기전 확인
#   1. 있으면
#       i) 그원의 다른 점이 현재 원 안에 있으면 ㅇㅋ
#       ii) 밖에 있으면 겹치는것 -> NO, break
#   2. s update
# 다 넣으면 YES

# 전체 coor을 다보는게 아닌 bisort로 x축 접점 idx만 저장했는데, 
# 더 느려짐

# 해결보고옴
# 괄호쌍 문제랑 비슷하게 풀면 되는거 였음..
# 메모리 제한 후한게 낚시였음


# 수학적으로 접근하지 않고 자료구조 위주로 풀기??

import sys

N = int(input())
no_flag = 0

stack = []
for i in range(N):
    x,r = map(int, sys.stdin.readline().split())
    stack.append((x+r, i))
    stack.append((x-r, i))

stack.sort()
stack2 = []
for _ in range(N*2):
    curr = stack.pop()
    if not stack2:
        stack2.append(curr)
        continue
    if stack2[-1][1] == curr[1]:
        stack2.pop()
        continue
    stack2.append(curr)
        
if stack2:
    print("NO")
else:
    print("YES")



