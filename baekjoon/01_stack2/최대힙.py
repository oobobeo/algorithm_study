# 11279

# heap 구현은 이딴식으로 하지 말고
# list index를 사용하는 방법을 사용하도록 하자


# input -> sys.stdin.readline().strip()

import sys

n = map(int, input().split())


class Node:
    def __init__(self, n):
        self.val = n
        self.left = None
        self.right = None

class MaxHeap:
    def __init__(self):
        self.root = None
        self.len = 0

    # when inserting, need inserting position
    # ex) 5(current) -> ['right','left']
    def len2direction(self):
        tier = 1
        while True:
            # print('while')
            # print(f"{2**(tier-1)} {self.len}")
            if 2**(tier)-1 >= self.len:
                break
            else:
                tier += 1

        # print(f"len: {self.len} tier: {tier}")
        direction = []
        if self.len == 2**tier -1: # tier full
            direction = ['left']*tier
            return direction
        else:
            target_pos = self.len - 2**(tier-1) + 2
            for i in range(tier-1):
                # print(f"target_pos: {target_pos}")
                if target_pos > 2**(tier-2-i): # go right
                    direction.append('right')
                    target_pos -= 2**(tier-2-i)
                else:
                    direction.append('left')
            return direction
            

    # insert Node with val=x to heap
    def insert(self, x):
        # print(x)
        nn = Node(x)
        if not self.root:
            self.root = nn
            self.len = 1
            return
        
        # node in heap
        node = self.root
        direction = self.len2direction()

        # print(f"x: {direction}")
        node_list = [self.root]
        for turn in range(len(direction)-1):
            if turn == 'left':
                node = node.left
            else:
                node = node.right
            node_list.append(node)
        if direction[-1] == 'left':
            node.left = nn
        else:
            node.right = nn
        
        self.len += 1

        # sort the nn
        node_list.reverse()
        rank = 0
        for node in node_list:
            if x > node.val:
                rank += 1
            else:
                break
        if rank == len(direction): # nn has the largest val
            self.root = nn

        node_list.append(node)
        print(f"rank: {rank} list: {node_list}")
        for i in range(rank):
            c = node_list.pop()
            p = node_list.pop()
            p_l = p.left
            p_r = p.right
            c_l = c.left
            c_r = c.right
            c.left = p_l
            c.right = p_r
            p.left = c_l
            p.right = c_r
            turn1 = direction.pop()
            if turn1 == 'left':
                c.left = p
            else:
                c.right = p
            
            if node_list:
                gp = node_list[-1]
                turn2 = direction[-1]
                if turn2 == 'left':
                    gp.left = c
                else:
                    gp.right = c
            node_list.append(c)
            


heap = MaxHeap()
for i in range(10):
    heap.insert(i)
        
        
print(heap.root.val)
print(heap.root.left.val)
print(heap.root.right.val)
print(heap.root.left.val)
print(heap.root.left.left.val)
print(heap.root.left.right.val)
print(heap.root.right.left.val)
print(heap.root.right.right.val)
print(heap.root.left.left.left.val)
print(heap.root.left.left.right.val)


