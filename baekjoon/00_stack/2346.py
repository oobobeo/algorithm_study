# 풍선 터뜨리기


class Node:
    def __init__(self, n):
        self.prev = self
        self.next = self
        self.val = n
        self.index = 1

class CircularQueue:
    def __init__(self, n):
        self.len = n
        if n == 0: return

        curr = self.curr = Node(1)
        if n == 1:
            self.curr = Node(1)
            self.curr.index = 0
        else:
            for i in range(n-1):
                next = Node(i+2)
                curr.next = next
                next.index = i+2
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


# set up balloons
iter_num = int(input())
values = list(map(int, input().split()))
dequeue = CircularQueue(iter_num)
curr = dequeue.curr
for i in range(iter_num):
    curr.val = values[i]
    curr = curr.next

# test
curr = dequeue.curr
for _ in range(iter_num):
    # print(f"index: {curr.index}, val: {curr.val}")
    curr = curr.next


# process balloons
result = []
# curr = dequeue.curr
for i in range(iter_num):
    # print(f"i: {i}, {dequeue.curr.index}:{dequeue.curr.val}")
    result.append(dequeue.curr.index)
    if i == iter_num - 1:
        break
    val = dequeue.curr.val
    dequeue.pop_curr()
    temp = dequeue.curr
    if val > 0:
        for _ in range(val-1):
            # print(_)
            # print(f"index: {temp.index}, val: {temp.val}")
            temp = temp.next
    else: # val < 0
        for _ in range(abs(val)):
            temp = temp.prev
    # print(f"index: {next.index}")
    dequeue.curr = temp

result = list(map(str, result))
print(' '.join(result))
