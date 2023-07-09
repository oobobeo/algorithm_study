from heapq import *
from functools import lru_cache
def solution(board):
    answer = 0
    r_len = len(board)
    
    '''
    dfs
    edge1) 같은 coor, 다른 direction
    '''
    dir = [(1,0),(0,-1),(-1,0),(0,1)]
    @lru_cache(maxsize=25*25)
    def _adj(pos,direction):
        x = pos[0]
        y = pos[1]
        cands = [(x+dir[i][0],y+dir[i][1],i) for i in range(4)]
        neis = []
        for c in cands:
            if c[0] >= 0 and c[0] <= r_len-1 and c[1] >= 0 and c[1] <= r_len-1 and board[c[0]][c[1]] == 0\
                and c[2] != (direction+2)%4: # 온곳으로 되돌아가기
                neis.append(c)
        return neis # [(x,y,dir)]
        
    
    # cost = prev_costs + cur_road_cost
    # nxt_cost = (corner_cost) + nxt_road_cost
    cost = [[[float("inf")]*4 for _ in range(r_len)] for _ in range(r_len)]
    cost[0][0] = [0,0,0,0]
    # vis[x][y][dir] = 0|1
    # vis = [[[0]*4 for _ in range(r_len)] for _ in range(r_len)]
    h = [(0,(0,0),0),(0,(0,0),3)] # heap. (cost, (x,y), direction)
    while h:
        c, cur, direction = heappop(h)
        if c > cost[cur[0]][cur[1]][direction]: # wasteful route
            continue
        for nei in _adj(cur,direction):
            new_c = c + 100 + ((direction-nei[2])%2)*500
            if new_c < cost[nei[0]][nei[1]][nei[2]]:
                cost[nei[0]][nei[1]][nei[2]] = new_c
                heappush(h, (new_c, (nei[0],nei[1]), nei[2]))
    # print(cost)
    # print(cost[r_len-1][r_len-1])
    return min(cost[r_len-1][r_len-1])