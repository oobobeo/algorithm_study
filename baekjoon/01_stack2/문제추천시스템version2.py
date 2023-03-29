# 21944

'''
ver1 응용이라 풀이 생각은 쉬웠다.
구현은 한 2시간 걸렸다..
각 cmd에서 필요한 연산랑을 O(logN) 밑으로 줄일수 있는 자료구조를 어떻게 잡아야 할까라는 생각을 하면서 풀었다.
L,G가 작은걸 캐치해서 아에 NxN list로 풀고, L보다 크거나 작은 문제는 애초에 L에 대해 sort되있는
    자료구조를 만들었다.
bst 사용하는 문제는 python에서는 double-ended-priorityqueue 로 푸는게 정해인듯.
L에 대한 탐색이 어차피 O(100)이여서 그냥 다 iter 해주면 되는 문제였다.
실제구현은 dict[*] = (min_heap, max_heap) 형태로 했다.
recommend 에서 사용하는 g2lp
recommend2,3 에서 사용하는 l2pg 를 따로 만들었다.
핵심 -> 어차피 add,solved는 problems로 각 problem이 valid한지 관리 해주면 되었다.
'''


import sys
from heapq import *
from collections import defaultdict


g2lp = {} # g2lp[g] = (min_heap, max_heap)[0] = [(l,p), ..]
l2pg = {} # l2pg[g] = (min_heap, max_heap)[0] = [(p,g), ..]
problems = {} # problems[p] = (l,g)

# init datastructures
for i in range(1,101):
    g2lp[i] = ([],[]) # min_heap, max_heap
for i in range(1,101):
    l2pg[i] = ([],[]) # min_heap, max_heap

# take initial data & sort
N = int(input())
for _ in range(N):
    p,l,g = map(int, sys.stdin.readline().split())
    problems[p] = (l,g)
    heappush(g2lp[g][0], (l,p)) # min
    heappush(g2lp[g][1], (-l,-p)) # max
    heappush(l2pg[l][0], (p,g)) # min
    heappush(l2pg[l][1], (-p,-g)) # max


# take cmds
M = int(input())
for _ in range(M):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'add': # p l g
        p,l,g = map(int, cmd[1:])
        heappush(g2lp[g][0], (l,p))
        heappush(g2lp[g][1], (-l,-p))
        heappush(l2pg[l][0], (p,g))
        heappush(l2pg[l][1], (-p,-g))
        problems[p] = (l,g)
        
    elif cmd[0] == 'solved':
        p = int(cmd[1])
        problems.pop(p)
        

    elif cmd[0] == 'recommend': # G x
        g,x = map(int, cmd[1:])
        minh, maxh = g2lp[g]
        if x == -1: # easiest, smallest
            while minh:
                l,p = minh[0]
                if p not in problems:
                    heappop(minh)
                    continue
                elif problems[p] != (l,g):
                    heappop(minh)
                    continue
                else:
                    print(p)
                    break
        else: # '1' hardest, biggest
            while maxh:
                l,p = maxh[0]
                l,p = -l,-p
                if p not in problems:
                    heappop(maxh)
                    continue
                elif problems[p] != (l,g):
                    heappop(maxh)
                    continue
                else:
                    print(p)
                    break


    elif cmd[0] == 'recommend2': # x
        x = int(cmd[1])
        result = None
        if x == 1:
            for l in range(100,0,-1):
                if l2pg[l]:
                    minh, maxh = l2pg[l]
                    while maxh:
                        p,g = maxh[0]
                        p,g = -p,-g
                        if p not in problems:
                            heappop(maxh)
                            continue
                        elif problems[p] != (l,g):
                            heappop(maxh)
                            continue
                        else:
                            result = p
                            break
                if result: break
        else: # x == -1
            for l in range(1,101):
                if l2pg[l]:
                    minh, maxh = l2pg[l]
                    while minh:
                        p,g = minh[0]
                        if p not in problems:
                            heappop(minh)
                            continue
                        elif problems[p] != (l,g):
                            heappop(minh)
                            continue
                        else:
                            result = p
                            break
                if result: break
        print(result)


    elif cmd[0] == 'recommend3': # x L
        x,L = map(int, cmd[1:])
        result = None
        if x == -1:
            for l in range(L-1,0,-1):
                if l2pg[l]:
                    minh, maxh = l2pg[l]
                    while maxh:
                        p,g = maxh[0]
                        p,g = -p,-g
                        if p not in problems:
                            heappop(maxh)
                            continue
                        elif problems[p] != (l,g):
                            heappop(maxh)
                        else:
                            result = p
                            break
                if result: break
        else: # x == '1'
            for l in range(L,101):
                if l2pg[l]:
                    minh, maxh = l2pg[l]
                    while minh:
                        p,g = minh[0]
                        if p not in problems:
                            heappop(minh)
                            continue
                        elif problems[p] != (l,g):
                            heappop(minh)
                        else:
                            result = p
                            break
                if result: break
        if result:
            print(result)
        else:
            print(-1)



