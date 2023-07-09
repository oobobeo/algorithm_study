def solution(gems):
    answer = []
    
    '''
    two-pointer
    edge1) 1 type of gem
    
    ''' 
    
    
    gem_set = set(gems)
    gem_count = {}
    cur_gems = set()
    for g in gem_set:
        gem_count[g] = 0
        
    i = j = 0
    gem_count[gems[0]] += 1
    cur_gems.add(gems[0])
    while j <= len(gems)-1:
        if len(cur_gems) == len(gem_set):
            answer.append((i,j))
            gem_count[gems[i]] -= 1
            if gem_count[gems[i]] == 0:
                cur_gems.remove(gems[i])
            i += 1
            continue
        else:
            j += 1
            if j >= len(gems):
                break
            gem_count[gems[j]] += 1
            
            cur_gems.add(gems[j])
            
    # print(answer)
    answer.sort(key=lambda x: (x[1]-x[0], x[0]))
    answer = answer[0]
    return [answer[0]+1,answer[1]+1]