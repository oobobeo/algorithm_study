from collections import defaultdict
def solution(enroll, referral, seller, amount):
    #        name.   parent.   
    # earned total_amount = 100*amount
    
    p = {}
    for child, parent in zip(enroll, referral):
        p[child] = parent
    
    
    def unroll(name, price):
        global n2p
        if price < 10 or name == '-':
            n2p[name] += price
            return
        
        tenth = price // 10
        n2p[name] += price - tenth
        unroll(p[name],tenth)
        
        
    
    global n2p
    n2p = defaultdict(int)
    for ss,aa in zip(seller,amount):
        unroll(ss,aa*100)
    
    answer = []
    for name in enroll:
        answer.append(n2p[name])
    
    return answer