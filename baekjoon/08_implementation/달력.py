# 20207


'''
한 2시간은 넘게 걸렸다... ㅠㅠ
문제를 2번 잘못 이해했다..
---
문제를 꼼꼼히 읽자!!! 특히 구현문제는 문제가 길어서 조건들을 대충 읽으면 안된다!

'''

from collections import defaultdict

N = int(input())

st2en = defaultdict(list)
en_num = defaultdict(int) # en_list[en] = num
for _ in range(N):
    # arr.append(list(map(int, input().split())))
    st,en = map(int, input().split())
    st2en[st].append(en)
    en_num[en] += 1


def chk_valid(level, st, length):
    for i in range(length):
        if arr[level][st+i] != 0:
            return False
    return True

def fill(level, st, length):
    for i in range(length):
        arr[level][st+i] = 1
    arr[level][st+length-1] = 2

# fill arr
arr = [[0]*366 for _ in range(N)]
for i in range(1,366):
    ens = sorted(st2en[i], reverse=True)
    if not ens: continue
    for en in ens:
        for level in range(N):
            if chk_valid(level, i, en-i+1):
                fill(level, i, en-i+1)
                break
            
# for l in range(3):
#     print(arr[l][0:14])

# calculate total
total = 0
cur_st = -1
max_width = 0
for i in range(366):
    # update max_width
    for lv in range(N-1,-1,-1):
        if arr[lv][i] == 1 or arr[lv][i] == 2:
            max_width = max(max_width, lv+1)
            if cur_st == -1:
                cur_st = i

    # chk if cur == end of block
    is_end = False
    if i == 365:
        is_end = True
    else:
        is_end = True
        for l in range(N):
            if arr[l][i+1] != 0:
                is_end = False

    if is_end:
        # print(i, max_width)
        total += (i-cur_st+1)*max_width
        cur_st = -1
        max_width = 0
        
print(total)
