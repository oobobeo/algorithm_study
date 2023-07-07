def solution(s):
    answer = []
    # print(eval(s))
    s_list = '[' + s[1:-1] + ']'
    s = eval(s_list)
    # print(eval(s_list))
    
    
    '''
    1. sort by len
    2. 
    '''
    s = sorted(s, key=lambda x: len(x))
    cur_set = set([])
    for cur in s:
        for x in cur:
            if x in cur_set: continue
            cur_set.add(x)
            answer.append(x)
    # print(answer)
    

    return answer