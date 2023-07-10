def solution(queue1, queue2):
    
    # xh x x x
    # ot     xt
    # o  o o oh
    
    '''
    N = 300,000
    ~O(N)
    경계선 최소로 움직이기
    1. total 구함
    2. total/2 구간들 찾기
        2-1. two-pointer
    3. 최소 움직이는 구간으로.
        head는 pop만, tail은 push만 가능 유의
    4. 가능한 구간 없으면 -1
    '''
    
    # 1. total
    total = sum(queue1) + sum(queue2)
    
    # 2. two-pointer
    # o o o o x x x o o o o
    # i       j
    target = total/2
    i = 0
    j = len(queue1)
    cur_sum = sum(queue1)
    cands = []
    q = queue1 + queue2
    q_len = len(queue1) + len(queue2)
    while i != q_len-1 and j != len(queue1)-1: # 1바퀴 돎
        if cur_sum == target:
            cands.append((i,j))
            i = (i+1)%(q_len)
        elif cur_sum < target:
            cur_sum += q[j]
            j = (j+1)%(q_len)
        elif cur_sum > target:
            cur_sum -= q[i]
            i = (i+1)%(q_len)
    # print(cands)
    
    # 3. 최소 움직이는 구간
    result = []
    for i,j in cands:
        if j >= len(queue1):
            result.append(i+j-len(queue1))
        else:
            result.append(i+ j+len(queue1)-len(queue2))
    # print(result)
    

    if result:
        return min(result)
    else:
        return -1