# 20440

N = int(input())
ts = []
for _ in range(N):
    s,e  = map(int, input().split())
    ts.append((s,-1)) # in
    ts.append((e,1))  # out
ts.sort(reverse=True)

record = 0
rs,re = 0,0
cur_count = 0
prv_count = 0
prv_t     = 0
i = 0
while ts:
    cur = ts.pop()
    cur_count += -cur[1]
    while ts and ts[-1][0] == cur[0]: # same time
        ccc = ts.pop()
        cur_count += -ccc[1]
    
    if cur_count == prv_count:
        continue
    elif prv_count < cur_count:
        # no need to update record
        prv_t = cur[0]
        prv_count = cur_count
    elif prv_count > cur_count:
        if prv_count > record:
            rs, re = prv_t, cur[0]
            record = prv_count
        prv_t = cur[0]
        prv_count = cur_count
        
    # print('>',cur[0], cur_count)

print(record)
print(rs,re)
