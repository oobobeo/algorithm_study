'''
double link 끊을때 반드시 체크해야할 것
a->b
1. front[a]
2. back[b]
3. lenght[src], length[dst]
4. conv_fb[c1], conv_fb[c2]


'''


import sys

Q = int(input())

SETUP = list(map(int, sys.stdin.readline().split()))
CMDS = []
for _ in range(Q):
    CMDS.append(tuple(map(int, sys.stdin.readline().split())))
N,M = SETUP[1:3] # N conv, M box

# set up boxes & conveyor
conv_fb = [[-1,-1] for _ in range(N+1)] # conveyor front/back [N+1][2]
front = [-1]*(M+2)   # [M+1], [-1]index for garbage values
back  = [-1]*(M+2)   # [M+1]
lengths = [-1]*(N+1) # [M+1]

conv_temp = [[] for _ in range(N+1)]
for n, c_id in enumerate(SETUP[3:]):
    conv_temp[c_id].append(n+1)
for c_id, boxes in enumerate(conv_temp):
    lengths[c_id] = len(boxes)
    if boxes:
        conv_fb[c_id][0] = boxes[0]
        conv_fb[c_id][1] = boxes[-1]
        if len(boxes) == 1:
            box = boxes[0]
            front[box] = -1
            back[box]  = -1
        else:
            front[boxes[0]] = -1
            back[boxes[-1]] = -1
            cur = boxes[0]
            for box in boxes[1:]:
                front[box] = cur
                cur = box
            cur = boxes[-1]
            for box in boxes[:-1][::-1]:
                back[box] = cur
                cur = box

# 2
def move_all(c_src, c_dst):
    # c_src = 0, c_dst = 0 
    if conv_fb[c_src][0] == -1 and conv_fb[c_dst][0] == -1:
        pass
    
    # c_src = 0, c_dst > 0
    elif conv_fb[c_src][0] == -1 and conv_fb[c_dst][0] != -1:
        pass
    
    # c_src > 0, c_dst = 0
    elif conv_fb[c_src][0] != -1 and conv_fb[c_dst][0] == -1:
        conv_fb[c_dst] = conv_fb[c_src][:]
        conv_fb[c_src] = [-1,-1]
        
    # c_src > 0, c_dst > 0
    elif conv_fb[c_src][0] != -1 and conv_fb[c_dst][0] != -1:
        dst_front = conv_fb[c_dst][0]
        src_back  = conv_fb[c_src][1]
        src_front = conv_fb[c_src][0]
        
        front[dst_front] = src_back
        back[src_back]   = dst_front
        
        conv_fb[c_dst][0] = src_front
        conv_fb[c_src] = [-1,-1]
        
    lengths[c_dst] += lengths[c_src]
    lengths[c_src] = 0
    return lengths[c_dst]
        
        
# 3
def replace_front(c_src, c_dst):
    # c_src = 0, c_dst = 0 
    if conv_fb[c_src][0] == -1 and conv_fb[c_dst][0] == -1:
        pass   
    
    # c_src = 0, c_dst > 0
    elif conv_fb[c_src][0] == -1 and conv_fb[c_dst][0] != -1:
        f = conv_fb[c_dst][0]
        b = back[f]
        if lengths[c_dst] > 1:
            conv_fb[c_dst][0] = b
            back[f] = -1
            front[b] = -1
            conv_fb[c_src] = [f,f]
        else: # lengths[c_dst] == 1
            conv_fb[c_dst] = [-1,-1]
            conv_fb[c_src] = [f,f]
            
        lengths[c_dst] -= 1
        lengths[c_src] += 1
    
    # c_src > 0, c_dst = 0
    elif conv_fb[c_src][0] != -1 and conv_fb[c_dst][0] == -1:
        f = conv_fb[c_src][0]
        b = back[f]
        if lengths[c_src] > 1:
            conv_fb[c_src][0] = b
            back[f] = -1
            front[b] = -1
            conv_fb[c_dst] = [f,f]
        else: # lengths[c_src] == 1
            conv_fb[c_src] = [-1,-1]
            conv_fb[c_dst] = [f,f]
            
        lengths[c_src] -= 1
        lengths[c_dst] += 1
        
    # c_src > 0, c_dst > 0
    elif conv_fb[c_src][0] != -1 and conv_fb[c_dst][0] != -1:
        f1 = conv_fb[c_src][0]
        b1 = back[f1]
        f2 = conv_fb[c_dst][0]
        b2 = back[f2]
        
        front[b1] = f2
        front[b2] = f1
        back[f1] = b2
        back[f2] = b1
        conv_fb[c_src][0] = f2
        conv_fb[c_dst][0] = f1
        
        if lengths[c_src] == 1:
            conv_fb[c_src] = [f2,f2]
        if lengths[c_dst] == 1:
            conv_fb[c_dst] = [f1,f1]
        
    return lengths[c_dst]

# 4
def move_half(c_src, c_dst):
    n = lengths[c_src] // 2
    if n == 0:
        pass
    else: # len(src) >= 2
        f1 = conv_fb[c_src][0]
        b1 = f1
        for _ in range(n-1):
            b1 = back[b1]
        f11 = back[b1]
        front[f11] = -1
        back[b1] = -1
        f2 = conv_fb[c_dst][0]
        
        # c_dst = 0
        if conv_fb[c_dst][0] == -1:
            conv_fb[c_dst] = [f1,b1]
            conv_fb[c_src][0] = f11
            front[f1] = -1
            back[b1] = -1
            
        # c_dst > 0
        elif conv_fb[c_dst][0] != -1:
            front[f2] = b1
            back[b1] = f2
            conv_fb[c_dst][0] = f1
            conv_fb[c_src][0] = f11
            
    lengths[c_src] -= n
    lengths[c_dst] += n    
    return lengths[c_dst]
    

# 5
def box_info(p_num):
    a = front[p_num]
    b = back[p_num]
    return a + 2*b
    
# 6
def conv_info(b_num):
    a,b = conv_fb[b_num]
    c = lengths[b_num]
    return a + 2*b + 3*c

for cmd in CMDS[:-1]:
    # print('[CMD]', cmd)
    if cmd[0] == 200:
        print(move_all(cmd[1],cmd[2]))
    elif cmd[0] == 300:
        print(replace_front(cmd[1],cmd[2]))
    elif cmd[0] == 400:
        print(move_half(cmd[1],cmd[2]))
    elif cmd[0] == 500:
        print(box_info(cmd[1]))
    elif cmd[0] == 600:
        print(conv_info(cmd[1]))
    
    
    # print('conv_fb', *[(i,x) for i,x in enumerate(conv_fb)], sep='\n')
    # print()
    # print('front', *[[i,x] for i,x in enumerate(front)], sep='\n')
    # print()
    # print('back ', *[[i,x] for i,x in enumerate(back)], sep='\n')
    # print()
    # print('lengths', *[[i,x] for i,x in enumerate(lengths)], sep='\n')
    
    # print('-------------------')

