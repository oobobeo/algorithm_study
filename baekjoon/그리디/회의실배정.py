# 1931





import sys

N = int(input())

meetings = {}
for _ in range(N):
    start, end = map(int, input().split())
    if end in meetings:
        meetings[end].append(start)
    else:
        meetings[end] = [start]

# sort end-time -> start-time

ends = list(meetings.keys())
ends.sort()

count = 0
curr_end = 0
for end in ends:
    # check start
    if curr_end <= end:
        for start in meetings[end]:
            if start >= curr_end and start != end: # found
                count += 1
                curr_end = end
                meetings[end].remove(start)
                break
        # 0 hours meeting
        while end in meetings[end]:
            count += 1
            meetings[end].remove(end)
            curr_end = end
        
print(count)


