# 7662






import sys
import heapq
from collections import defaultdict

T = int(input())
for _ in range(T):
    k = int(input())
    # keys = []
    # counter = collections.Counter()
    max_heap = []
    min_heap = []
    counter = defaultdict(int)
    for _ in range(k):
        cmd, n = sys.stdin.readline().split()
        n = int(n)
        if cmd == 'I':
            heapq.heappush(max_heap, -n)
            heapq.heappush(min_heap, n)
            counter[n] += 1
        else: # cmd == 'D'
            if n == -1: # pop min
                while min_heap:
                    supposed_min = heapq.heappop(min_heap)
                    if counter[supposed_min] > 0:
                        counter[supposed_min] -= 1
                        break
            else: # pop max
                while max_heap:
                    supposed_max = heapq.heappop(max_heap)
                    if counter[-supposed_max] > 0:
                        counter[-supposed_max] -= 1
                        break

    while max_heap and counter[-max_heap[0]] == 0: heapq.heappop(max_heap)
    while min_heap and counter[min_heap[0]] == 0: heapq.heappop(min_heap)

    if max_heap:
        print(-max_heap[0], min_heap[0], sep=' ')
    else:
        print("EMPTY")
