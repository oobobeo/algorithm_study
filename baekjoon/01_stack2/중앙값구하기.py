# 수열 -> 홀수번째 마다 지금까지의 중앙값 출력
'''
어디선가 비슷한 문제를 봐서 쉽게 풀었다.
들어오는 수를 lheap[], rheap[] 으로 나눠 받으면 항시 중간값을 O(1)에 알수 있다.
heap의 push: O(1), top_seek: O(1) 임을 이용해 주었다.
새로운 수 2개가 들어오면 mid값(-lheap[0]) 과 비교해서 lheap, rheap중 어디에 push할지 알 수 있다.
'''

import sys
from bisect import *
from heapq import *

T = int(input())
for _ in range(T):
    lheap = [] # max heap
    rheap = [] # min heap
    M = int(input())
    if M == 1:
        print(1)
        print(input())
        continue

    n = M//2 + 1

    arr = []
    for i in range((M//10)+1):
        line = list(map(int,sys.stdin.readline().split()))
        arr += line

    # initial setup
    heappush(lheap, -arr[0])
    result = [-lheap[0]]
    for i in range(1,M,2): # i = 3,5,7, ..
        # push to heaps
        if arr[i] <= -lheap[0]:
            heappush(lheap, -arr[i])
        else:
            heappush(rheap, arr[i])
        if arr[i+1] <= -lheap[0]:
            heappush(lheap, -arr[i+1])
        else:
            heappush(rheap, arr[i+1])

        # sort heaps
        if len(lheap) <= len(rheap):
            heappush(lheap, -heappop(rheap))
        elif len(lheap) != len(rheap)+1:
            heappush(rheap, -heappop(lheap))

        result.append(-lheap[0])

    # print(arr)
    print(n)
    for i in range((len(result)-1) // 10 + 1):
        print(*result[10*(i):10*(i)+10])


