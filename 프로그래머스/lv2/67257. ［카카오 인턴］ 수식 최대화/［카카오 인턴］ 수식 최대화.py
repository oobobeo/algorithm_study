def solution(expression):
    exp = []
    temp1 = []
    temp = expression.split('-')
    for tt in temp:
        temp1.append(tt)
        temp1.append('-')
    temp1.pop()
    temp2 = []
    for t1 in temp1:
        t1 = t1.split('+')
        for tt1 in t1:
            temp2.append(tt1)
            temp2.append('+')
        temp2.pop()
    for t2 in temp2:
        t2 = t2.split('*')
        for tt2 in t2:
            exp.append(tt2)
            exp.append('*')
        exp.pop()
    
    # order: a -> b -> c
    def _calc(exp,a,b,c):
        ans = 0
        while a in exp:
            idx = exp.index(a)
            new_num = eval(''.join(exp[idx-1:idx+2]))
            exp = exp[:idx-1] + [str(new_num)] + exp[idx+2:]
        while b in exp:
            idx = exp.index(b)
            new_num = eval(''.join(exp[idx-1:idx+2]))
            exp = exp[:idx-1] + [str(new_num)] + exp[idx+2:]
        while c in exp:
            idx = exp.index(c)
            new_num = eval(''.join(exp[idx-1:idx+2]))
            exp = exp[:idx-1] + [str(new_num)] + exp[idx+2:]
        return int(exp[0])
    
    
    
    answer = []
    print(_calc(exp,'-','+','*'))
    answer = max(abs(_calc(exp,'-','+','*')),
                abs(_calc(exp,'-','*','+')),
                abs(_calc(exp,'+','-','*')),
                abs(_calc(exp,'+','*','-')),
                abs(_calc(exp,'*','+','-')),
                abs(_calc(exp,'*','-','+')),
                )
    return answer