import re
from itertools import product
def solution(user_id, banned_id):
    answer = 0
    
    total = []
    for bid in banned_id:
        ptn = '^' + ''.join([x if x != '*' else '[a-z0-9]' for x in bid ]) + '$'
        count = []
        for uid in user_id:
            # print(re.findall(ptn, uid))
            if re.findall(ptn, uid):
                count.append(uid)
        total.append(count)
    
    # print(total)
    combs = [x for x in product(*total)]
    result = set()
    for c in combs:
        # print('c', c)
        if len(set(c)) < len(total): continue
        c = list(c)
        c.sort()
        result.add(''.join(c))
    # print()
    # print(result)
    
    return len(result)