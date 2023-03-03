# in python
# list.pop() is O(N)
# which results in total of O(NM)

# deque provides O(1) way of dealing with elements on the front, back

# 큐2
import sys
from collections import deque
queue = deque()

iter_length = int(sys.stdin.readline())
for _ in range(iter_length):
    cmd = sys.stdin.readline().split()
    if len(cmd) >= 2: # push x
        n = cmd[1]
        queue.append(n)
    else: # else
        if cmd[0] == 'back':
            print(queue[-1]) if queue else print(-1)
        elif cmd[0] == 'front':
            print(queue[0]) if queue else print(-1)
        elif cmd[0] == 'empty':
            print(0) if queue else print(1)
        elif cmd[0] == 'size':
            print(len(queue))
        else: # pop
            if queue:
                print(queue.popleft())
            else:
                print(-1)


# a - b - c - d