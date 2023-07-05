def solution(n, info):
    from itertools import product, combinations
    answer = []
    '''
    1. k점을 더많이 맞춘사람이 k점을 가져감
        1-1. 동일하면 어피치가 가져감
    2. 마지막점수가 더 커야됨
        2-1. 동일하면 어피치 우승
    가장 큰 점수차이로 이기는 경우 return
    없으면 [-1]
    '''
    
    info_asc = info[::-1]
    # 1. validate comb
    # 2. calculate scorediff
    def validate_and_scorediff_arr(comb):
        scorediff = 0
        used = 0
        arr = [0, 0,0,0,0,0, 0,0,0,0,0] # 0-10
        for c in comb:
            used += (info_asc[c] + 1)
            arr[c] += (info_asc[c] + 1)
        if used > n:
            return False
        # calculate scorediff
        for i in range(11):
            if arr[i] == 0 and info_asc[i] == 0: 
                continue
            if arr[i] > info_asc[i]: 
                scorediff += i
            else: 
                scorediff -= i
        
        if used == n:
            return (scorediff, arr)
        elif used < n: # 덜 씀
            arr[0] += (n-used)
            return (scorediff, arr)
    
    
    cands = []
    # for nn in range(1, 4): # pick 1 ~ n 점수판
    for nn in range(1, n+1): # pick 1 ~ n 점수판
        combs = combinations([10,9,8,7,6,5,4,3,2,1,0],r=nn)
        for c in combs:
            sa = validate_and_scorediff_arr(c)
            if sa:
                cands.append([sa[0]] + sa[1])
                
    if cands:
        cands.sort(reverse=True)
        print(0, cands[0])
        print(-1, cands[-1])
        print('----------')
        scorediff, arr = cands[0][0], cands[0][1:]
        # print(scorediff, arr)
        if scorediff <= 0:
            return [-1]
        else:
            return arr[::-1]
    else:
        return [-1]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     target = 0
#     for i in range(10,-1,-1):
#         target += i*info[i]
        
#     combs = product([10,9,8,7,6,5,4,3,2,1,0],repeat=n)
#     result = [] # [[score,0th,1th,..10th]]
#     for c in combs:
#         score = 0
#         arr = [0,0,0,0,0, 0,0,0,0,0, 0] # 0-10
#         for val in c:
#             arr[val] += 1
#         for i in range(11): # 0~10
#             if arr[i] > info[10-i]:
#                 score += i
#         # cc = list(c)
#         # cc.reverse()
#         # print([score] + arr)
#         result.append([score] + arr)
    
#     result.sort(reverse=True)
#     result = result[0]
#     print(result)
#     answer = result[1:]
#     answer.reverse()
#     score = result[0]
#     if score > target:
#         return answer
#     else:
#         return [-1]
    
    
    
    