# 요세푸스 문제

# (7.3) : 1-2-3-4-5-6-7 : <3,6,2,7,5,1,4>
# brute force turned out to be not a O(N^2)


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



n, k = map(int, input().split())


queue = CircularQueue(n)
result = []
while queue.len > 0:
    for _ in range(k-1):
        queue.curr = queue.curr.next
    result.append(queue.pop_curr())

output = "<"
for x in result:
    output = output + str(x) + ", "
output = output[:-2] + ">"
print(output)