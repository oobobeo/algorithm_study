import sys
sys.setrecursionlimit(1024*200)

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
ops_ = list(map(int, sys.stdin.readline().split()))

results = []

def func(c_val, ops, idx):
    idx += 1
    if idx == N-1:
        if ops[0]:
            results.append(c_val+arr[idx])
        elif ops[1]:
            results.append(c_val-arr[idx])
        elif ops[2]:
            results.append(c_val*arr[idx])
        elif ops[3]:
            temp = 0
            if c_val < 0:
                temp = -(-c_val//arr[idx])
            else:
                temp = c_val//arr[idx]
            results.append(temp)
        return
    if ops[0]:
        ops[0] -= 1
        func(c_val+arr[idx], ops, idx)
        ops[0] += 1
    if ops[1]:
        ops[1] -= 1
        func(c_val-arr[idx], ops, idx)
        ops[1] += 1
    if ops[2]:
        ops[2] -= 1
        func(c_val*arr[idx], ops, idx)
        ops[2] += 1
    if ops[3]:
        ops[3] -= 1
        if c_val < 0:
            temp = -(-c_val//arr[idx])
        else:
            temp = c_val//arr[idx]
        func(temp, ops, idx)
        ops[3] += 1
    
    
func(arr[0], ops_, 0)
# print(results)
print(max(results))
print(min(results))
