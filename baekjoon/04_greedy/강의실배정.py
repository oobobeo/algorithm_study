# 11000


'''
정렬을 (start_time, end_time) 혹은 (end_time, start_time)으로 정렬할 수 있다.

클래스가 1개이고, 최대한의 강의를 끼워넣는 문제는 정렬을 (en,st)로 했다.
하지만, 이 문제는 이렇게 정렬하면 한번 강의를 끼워넣을 때마다
classroom 정렬을 해야되서 최악의 경우 O(N^2) 이다.

<풀이>
(st,en)으로 정렬하고, min-heap을 사용하면, O(NlogN)으로 풀린다.

수업을 넣을 떄, room중 가장 작은 값과만 비교하면 된다.
    case1) room중 가장 작은값 > 수업 st값. (가능한 room x)
        room 추가
    case2) room중 가장 작은값 <= 수업 st값
        room중 가장 작은값 = 수업 en 값으로 치환.
        
<중요>
    수업을 (st,en)으로 정렬했으므로, st1 < st2 < st3 < .. 보장됨.
    현재 수업 st값보다 작은 room 값들은 수업을 넣는 입장에서는 다 상관이 없이 똑같음.
    따라서, 수업을 넣을 때, room의 가장 작은값만 비교해도됨.
        (가능 한 room중 가장 값 큰거 안찾아도 됨.)
'''


import sys
import heapq

# MAX = 10**10
N = int(input())

ts = []
for _ in range(N):
    s,t = map(int, sys.stdin.readline().split())
    ts.append((s,t))
heapq.heapify(ts)

room = [0] # min-heap. endtimes for each classes.
while ts:
    s,t = heapq.heappop(ts)
    min_end_time = heapq.heappop(room)
    if min_end_time <= s:
        heapq.heappush(room, t)
    else:
        heapq.heappush(room, min_end_time)
        heapq.heappush(room, t)

print(len(room))


'(end_time, start_time) 으로 정렬한 풀이. timeout 된다.'
# def sift_up(room,l,r):
#     i = l
#     while i<r:
#         room[i],room[i+1] = room[i+1],room[i]
#         i += 1
# def sift_down(room,l,r):
#     i = r
#     while l<i:
#         room[i],room[i-1] = room[i-1],room[i]
#         i -= 1

# ts = []
# for _ in range(N):
#     s,t = map(int, sys.stdin.readline().split())
#     ts.append((t,s))
# ts.sort(reverse=True)
# # print(ts)
# room = [0] # ending time for each room(idx)
# while ts:
#     t,s = ts.pop()
#     l = bisect.bisect_right(room, s) - 1
#     r = bisect.bisect_right(room, t) - 1
#     if l == -1: # no room available
#         # append at the end and sift_down
#         room.append(t)
#         sift_down(room,r+1,len(room)-1)
#     else:
#         room[l] = t
#         # [l,r] 구간에 대해, l를 r까지 올려야됨
#         sift_up(room,l,r)

#     # print(s,t,room)

# # result
# print(len(room))


