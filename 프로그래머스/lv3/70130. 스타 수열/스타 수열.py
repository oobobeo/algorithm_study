from collections import defaultdict
def solution(arr):
    if len(arr) == 1:
        return 0
    
    occurance = defaultdict(int)
    for x in arr:
        occurance[x] += 1
    occurance = [(occur,n) for n,occur in occurance.items()]
    occurance.sort(reverse=True)
    # print('0', occurance)
    
    ans = 0
    for o, num in occurance:
        if o < ans:
            break
        state = -1 # -1: grab any, 0: grab num, 1: grab not num
        pair_c = 0 # pair_c
        for x in arr:
            if state == 0 and x == num:
                state = -1
                pair_c += 1
            elif state == 1 and x != num:
                state = -1
                pair_c += 1
            else: # state == -1
                if x == num:
                    state = 1
                else:
                    state = 0
        ans = max(ans,pair_c)
                
    return ans*2