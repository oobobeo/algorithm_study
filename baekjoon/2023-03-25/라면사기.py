# 18185

# Ai = 3
# Ai + Ai+1 = 5
# Ai + Ai+1 + Ai+2 = 7

# 그리디로 
# 3개 연속인것 최대로 ㅆ고
# 2개 연속인것 최대로 쓰고
# 1개 연속인것 최대로 쓰면 됨.

# 가장 숫자 큰것부터.
# 12121 같이 같은 숫자가 2칸이하로 띄어져 있으면 동시에 포함해야됨.
# -> 3기둥 합이 가장 큰것부터 하면 되는거 같음.


import sys
import functools

N = int(input())

arr = list(map(int, sys.stdin.readline().split()))

result = 0

# i: level
# i=0: 꼭대기
# i=999: 바닥

# 3개
md = [(-1,-1)]*(N-2) # [(3개 합 값, idx), ..]
for k in range(N-2):
    md[k] = (arr[k] + arr[k+1] + arr[k+2], k)
# md.sort()
for peak in range(max(arr),0,-1):
    slct_bl = [] # selected blocks from md

    # peaks
    peaks = set()
    # peak = max(arr)
    for j in range(N):
        if arr[j] == peak:
            peaks.add(j)

    if not peaks: continue # empty level

    # peak -> md_candidates -> sort
    md_cand = set()
    for p in peaks:
        if p >= 2:
            md_cand.add(p-2)
            md_cand.add(p-1)
            md_cand.add(p)
        elif p >= 1:
            md_cand.add(p-1)
            md_cand.add(p)
        else: # p >= 0
            md_cand.add(p)
    md_cand = [md[mdc] for mdc in md_cand]
    md_cand.sort()

    # for st, idx in md[::-1]: # sub_total, idx
    for a in range(len(md_cand)-1,-1,-1):
        st, idx = md_cand[a]
        if idx in peaks or idx+1 in peaks or idx+2 in peaks:
            if arr[idx] > 0 and arr[idx+1] > 0 and arr[idx+2] > 0:
                slct_bl.append(idx)
                peaks.discard(idx)
                peaks.discard(idx+1)
                peaks.discard(idx+2)
                arr[idx] -= 1
                arr[idx+1] -= 1
                arr[idx+2] -= 1
        if not peaks: break

    result += len(slct_bl)*7

    # prepare md
    for k in range(N-2):
        md[k] = (arr[k] + arr[k+1] + arr[k+2], k)
    # md.sort()


# 2개
md = [(-1,-1)]*(N-1) # [(3개 합 값, idx), ..]
for k in range(N-1):
    md[k] = (arr[k] + arr[k+1], k)
# md.sort()
for peak in range(max(arr),0,-1):
    slct_bl = [] # selected blocks from md

    # peaks
    peaks = set()
    # peak = max(arr)
    for j in range(N):
        if arr[j] == peak:
            peaks.add(j)

    if not peaks: continue # empty level

    # peak -> md_candidates -> sort
    md_cand = set()
    for p in peaks:
        if p >= 2:
            md_cand.add(p-2)
            md_cand.add(p-1)
            md_cand.add(p)
        elif p >= 1:
            md_cand.add(p-1)
            md_cand.add(p)
        else: # p >= 0
            md_cand.add(p)
    md_cand = [md[mdc] for mdc in md_cand]
    md_cand.sort()

    # for st, idx in md[::-1]: # sub_total, idx
    for a in range(len(md_cand)-1,-1,-1):
        st, idx = md_cand[a]
        if idx in peaks or idx+1 in peaks:
            if arr[idx] > 0 and arr[idx+1] > 0:
                slct_bl.append(idx)
                peaks.discard(idx)
                peaks.discard(idx+1)
                arr[idx] -= 1
                arr[idx+1] -= 1
        if not peaks: break

    result += len(slct_bl)*5
    
    # prepare md
    for k in range(N-1):
        md[k] = (arr[k] + arr[k+1], k)
    # md.sort()


# 나머지 1개 남은것들
ones = functools.reduce(lambda x,y: x+y, arr)
result += ones*3

# result
print(result)



