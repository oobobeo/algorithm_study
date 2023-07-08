import bisect
import heapq as hq
from collections import defaultdict
def solution(k, room_number):
    
    nxt = {}
    answer = []
    for n in room_number:
        idx = n
        update = []
        while True:
            # collision
            nxt_idx = nxt.get(idx,None)
            if not nxt_idx:
                nxt[idx] = (idx+1)
                answer.append(idx)
                break
            update.append(idx)
            idx = nxt_idx
        for u in update:
            nxt[u] = (idx+1)

    
    
    
    
    return answer
