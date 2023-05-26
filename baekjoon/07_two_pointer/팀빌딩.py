# 22945

import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))

# edge
if N == 2:
    print(0)
    exit(0)

# init
i = 0
j = N-1
cur_val = (j-i-1)*min(arr[i],arr[j])
vals = [cur_val]

# 2_pointer
while i+1 < j:
    print('i j', i,j)
    if arr[i] > arr[j]:
        j -= 1
        cur_val = (j-i-1)*min(arr[i],arr[j])
        vals.append(cur_val)
    elif arr[i] < arr[j]:
        i += 1
        cur_val = (j-i-1)*min(arr[i],arr[j])
        vals.append(cur_val)
    else: # arr[i] == arr[j]
        # k x x x k
        # k x k
        if arr[i+1] > arr[j-1]:
            i += 1
            cur_val = (j-i-1)*min(arr[i],arr[j])
            vals.append(cur_val)
        elif arr[i+1] < arr[j-1]:
            j -= 1
            cur_val = (j-i-1)*min(arr[i],arr[j])
            vals.append(cur_val)
        else:
            i += 1 # or j -= 1. doesn't matter
            cur_val = (j-i-1)*min(arr[i],arr[j])
            vals.append(cur_val)
print(max(vals))





