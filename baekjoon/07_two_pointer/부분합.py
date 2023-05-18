# 1806

'''
edgecase 들을 적어가면서 했는데,
edge3 을 놓쳐서 틀렸다..

edgecase 찍어가면서 하자
'''

import sys

N,S = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))

length = 1000000 # inf

# init
# edge3) arr[0] >= S
st,en = 0,0
cur_sum = arr[0]
if cur_sum >= S:
    length = 1

# main
# edge1) st > en
while en <= N-2:
    en += 1
    cur_sum += arr[en]
    if cur_sum < S: continue
    
    # cur_sum >= S
    while cur_sum >= S and st < en:
        if cur_sum - arr[st] >= S:
            cur_sum -= arr[st]
            st += 1
        else:
            break

    length = min(length, en-st+1)
    

        
# edge2) no possible sub_array
if length == 1000000:
    print(0)
else:
    print(length)




