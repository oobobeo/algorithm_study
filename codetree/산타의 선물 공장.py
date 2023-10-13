
import sys
from collections import deque

Q = int(input())
temp = list(map(int, sys.stdin.readline().split()))
N,M = temp[1],temp[2]
IDS = temp[3:3+N]
WS = temp[3+N:]

CMDS = []
for _ in range(Q-1):
    CMDS.append(tuple(map(int, sys.stdin.readline().split())))

###
workings = [1]*M   # working[belt_id] = 0|1
id_w = {}          # id_w[box_id]     = box_w
belt_box_list = [] # belt[M]          = deque([box_ids])
belt_box_set = []  # belt_boxes[M]    = set([box_ids])
belt_box_idx = [0]*M
###
for id,w in zip(IDS,WS):
    id_w[id] = w
for i in range(M):
    temp = IDS[i*(N//M):(i+1)*(N//M)]
    belt_box_list.append(deque(temp))
    belt_box_set.append(set(temp))
###
# print()
# print('id_w')
# print(id_w)
# print()

# class box:
#     def __init__(self, i):
#         self.nxt = None
#         self.prv = None

# class belt:
#     def __init__(self, idx):
#         self.len = N//M
#         self.cur = None
#         self.nxt = None
#         self.prv = None
    
#     def absorb(self, other):
#         self.len += other.len
#         if self.len == 1:
#             self.cur.nxt = other.cur
#             other.cur.prv = self.cur
#         else:
#             self.cur.prv.nxt = other.cur
#             other.cur.prv = self.cur.prv

def belt_box_cur(belt_id):
    b_i = belt_box_idx[belt_id]
    return b_i

def belt_box_next(belt_id):
    l = len(belt_box_list)
    b_i = (belt_box_idx[belt_id] + 1) % l
    belt_box_idx[belt_id] = b_i
    return b_i
    

for cmd in CMDS:
    # print()
    # print('cmd', cmd)
    # print(belt_box_list)
    # print(belt_box_set)
    
    
    if cmd[0] == 200:   # w_max
        w_max = cmd[1]
        total_w = 0
        for idx in range(M):
            while len(belt_box_list[idx]) > 0 and belt_box_list[idx][0] not in belt_box_set[idx]:
                # print('box already gone')
                belt_box_list[idx].popleft()
            # while len(belt_box_list[idx]) > 0 and belt_box_cur(idx) not in belt_box_set[idx]:
            #     # print('box already gone')
            #     belt_box_list[idx].popleft()
            
                
            if len(belt_box_list[idx]) == 0:
                continue 
            box_id = belt_box_list[idx].popleft()
            if id_w[box_id] <= w_max:
                total_w += id_w[box_id]
                belt_box_set[idx].remove(box_id)
            else:
                belt_box_list[idx].append(box_id)
        print(total_w)
                
    elif cmd[0] == 300: # r_id
        r_id = cmd[1]
        flag = False
        for idx in range(M):
            if r_id in belt_box_set[idx]:
                flag = True
                belt_box_set[idx].remove(r_id)
                break
        if flag:
            print(r_id)
        else:
            print(-1)
            
    elif cmd[0] == 400: # f_id
        f_id = cmd[1]
        flag = False
        for idx in range(M):
            if f_id in belt_box_set[idx]:
                flag = True
                
                # while belt_box_list[idx][0] != f_id:
                #     belt_box_list[idx].append(belt_box_list[idx].popleft())
                    
                while belt_box_list[idx][0] != f_id:
                    cur = belt_box_list[idx].popleft()
                    if cur in belt_box_set[idx]:
                        belt_box_list[idx].append(cur)
                
                break
        if flag:
            print(idx+1)
        else:
            print(-1)
        
    elif cmd[0] == 500: # b_num
        b_num = cmd[1] - 1
        if workings[b_num] == 0:
            print(-1)
        else:
            workings[b_num] = 0
            # 1. find working belt
            # 2. relocate boxes
            for idx_alpha in range(b_num,b_num+M):
                idx = idx_alpha % M
                # print('idx, b_num', idx, b_num)
                if workings[idx] == 1:
                    belt_box_list[idx] += belt_box_list[b_num]
                    belt_box_set[idx] |= belt_box_set[b_num]
                    belt_box_list[b_num] = []
                    belt_box_set[b_num] = set()
                    break
            print(b_num+1)

