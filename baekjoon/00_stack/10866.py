# 덱


import sys


class Node:
    def __init__(self, n):
        self.prev = self
        self.next = self
        self.val = n

class CircularQueue:
    def __init__(self, n):
        self.len = n
        if n == 0: return

        curr = self.curr = Node(1)
        if n == 1:
            self.curr = Node(1)
        else:
            for i in range(n-1):
                next = Node(i+2)
                curr.next = next
                next.prev = curr
                curr = next
            curr.next = self.curr
            self.curr.prev = curr

    
    def pop_curr(self):
        if self.len == 0:
            return -1
        temp = self.curr.val
        if self.len >= 3:
            prev = self.curr.prev
            next = self.curr.next
            prev.next = next
            next.prev = prev
            self.curr = next
        elif self.len == 2:
            self.curr = self.curr.next
            self.curr.prev = self.curr.next = self.curr
        elif self.len == 1:
            self.curr = None

        self.len -= 1
        return temp


queue = CircularQueue(0)

for _ in range(int(input())):
    cmd = sys.stdin.readline().split()
    if len(cmd) == 2: # push_front x, push_back x
        nn = Node(cmd[1])
        if queue.len == 0:
            queue.curr = nn
        else:
            head = queue.curr
            tail = queue.curr.prev
            nn.next = head
            head.prev = nn
            tail.next = nn
            nn.prev = tail

        if cmd[0] == 'push_front':
            queue.curr = nn
        else: # push_back x
            pass
        queue.len += 1

    else:
        if cmd[0] == 'pop_front':
            print(queue.pop_curr())
        elif cmd[0] == 'pop_back':
            if queue.len == 0:
                print(-1)
                continue
            queue.curr = queue.curr.prev
            print(queue.pop_curr())
        elif cmd[0] == 'size':
            print(queue.len)
        elif cmd[0] == 'empty':
            print(0) if queue.len else print(1)
        elif cmd[0] == 'front':
            if queue.len:
                print(queue.curr.val)
            else:
                print(-1)
        elif cmd[0] == 'back':
            if queue.len:
                print(queue.curr.prev.val)
            else:
                print(-1)











