# 카드2

# 오이디프수 의 circular queue 그대로 사용


class Node:
    def __init__(self, n):
        self.prev = None
        self.next = None
        self.val = n

class CircularQueue:
    def __init__(self, n):
        self.len = n
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



n = int(input())


queue = CircularQueue(n)
while queue.len >= 2:
    queue.pop_curr()
    queue.curr = queue.curr.next


print(queue.curr.val)

# 123456
# 34562
# 5624
# 246
# 64
# 4