# 21939




'''
1. recommend는 "출력한다"여서 heap[0] 해줘야되는데 pop했다.
    3시간 넘게 여기서 소비된듯
2. add,remove,add,remove를 한 p에 대해 해주면 heap에는 (*,p)가 쌓인다
    이를 recommend때 잡아줘야되는데 이상하게 해서 또 시간소비.
3. bst없으면 priority queue 2개 쓰는게 정해인거 같다.
'''
'''
<풀이>
min_heap, max_heap에 (l,p) 넣어줘서 seek(min, max)를 빠르게 해줌.
같은 p가 recommend로 정리되지 않은채 add,remove가 여러번 될 수 있으므로,
    problems{}에 해당 p에 해당하는 valid한 l값 1개를 tracking해줌
recommend x 일 때, valid하지 않은 p를 만나거나, problem자체에 등록되지
    않은 p를 만나면 heappop해줌.
'''



import sys
from heapq import *
from collections import defaultdict

# l2p = defaultdict(list) # l2p[l] = [1,2,3,4..]
# p2l = {} # p2l[p] = l
# levels = [] # sorted
min_heap = []
max_heap = []
problems = {} # keep track of all problems

N = int(input())
for _ in range(N):
    p,l = map(int, sys.stdin.readline().split())
    problems[p] = l
    min_heap.append((l,p))
    max_heap.append((-l,-p))
heapify(min_heap)
heapify(max_heap)


M = int(input())
for _ in range(M):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'add':
        p,l = map(int, cmd[1:])
        heappush(min_heap, (l,p))
        heappush(max_heap, (-l,-p))
        problems[p] = l
        
    elif cmd[0] == 'recommend':
        if cmd[1] == '-1': # easiest, smallest
            while min_heap:
                l,p = min_heap[0]
                if p not in problems:
                    heappop(min_heap)
                    continue
                elif problems[p] != l:
                    heappop(min_heap)
                    continue
                else: # exist && valid
                    print(p)
                    break
        else: # '1' hardest, biggest
            while max_heap:
                l,p = max_heap[0]
                l,p = -l,-p
                if p not in problems:
                    heappop(max_heap)
                    continue
                elif problems[p] != l:
                    heappop(max_heap)
                    continue
                else: # exist && valid
                    print(p)
                    break
    else: # 'solved'
        p = int(cmd[1])
        problems.pop(p)



