def solution(cap, n, deliveries, pickups):
    answer = 0
    
    # cap
    # n: num of houses
    # deliveries: num of delivery for (i+1)'th house
    # pickups:    num of pickups  for (i+1)'th house
    
    
    # 한번 k 까지 갔다옴. dist=k*2
    # deliveries, pickups 따로 오른쪽 부터 충족시켜주기.
    
    # deliveries[d]
    # pickups[p]
    
    d,p = n-1,n-1
    while True:
        d_max, p_max = -1, -1
        flag_d = flag_p = 0
        cur_d = cur_p = 0
        
        
        # deliveries
        while cur_d < cap and d >= 0:
            if deliveries[d] == 0:
                d -= 1
                continue
            if flag_d == 0:
                flag_d = 1
                d_max = d
            deliveries[d] -= 1
            cur_d += 1
        
        # pickups
        while cur_p < cap and p >= 0:
            if pickups[p] == 0:
                p -= 1
                continue
            if flag_p == 0:
                flag_p = 1
                p_max = p
            pickups[p] -= 1
            cur_p += 1
            
            
            
        answer += (max(d_max, p_max)+1)*2
        # print(d,p)
        # print(cur_d,cur_p)
        # print(deliveries, pickups)
        
        if d == -1 and p == -1:
            break
    
    
    return answer

print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
