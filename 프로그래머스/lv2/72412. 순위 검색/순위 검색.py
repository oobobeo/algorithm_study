import bisect
def solution(info, query):
    # score[3][2][2][2]
    # cpp,java,python
    # backend,frontend
    # junior, senior
    # chicken, pizza
    t = {'cpp': 0, 'java':1, 'python':2,
        'backend': 0, 'frontend': 1,
        'junior': 0, 'senior': 1,
        'chicken': 0, 'pizza': 1,
        '-':'-'}
    score = [[[[[],[]] for _ in range(2)] for __ in range(2)] for ___ in range(3)]
    
    for cmd in info:
        a,b,c,d,s = cmd.split()
        score[t[a]][t[b]][t[c]][t[d]].append(int(s))
        score[t[a]][t[b]][t[c]][t[d]].sort()
    
    answer = []
    for q in query:
        a,_,b,_,c0,_,d,s = q.split()
        s = int(s)
        categ = [[t[a],t[b],t[c0],t[d]]]
        # print(categ)
        new = []
        if t[a] == '-':
            while categ:
                c = categ.pop()
                new.append([0,*c[1:]])
                new.append([1,*c[1:]])
                new.append([2,*c[1:]])
            categ = new
            
        new = []
        if t[b] == '-':
            while categ:
                c = categ.pop()
                new.append([c[0], 0,*c[2:]])
                new.append([c[0], 1,*c[2:]])
            categ = new
                
        new = []
        if t[c0] == '-':
            while categ:
                c = categ.pop()
                new.append([c[0], c[1], 0,c[3]])
                new.append([c[0], c[1], 1,c[3]])
            categ = new
                
        new = []
        if t[d] == '-':
            while categ:
                c = categ.pop()
                new.append([c[0], c[1],c[2], 0])
                new.append([c[0], c[1],c[2], 1])
            categ = new
                
        # count
        temp = 0
        for c in categ:
            temp += (len(score[c[0]][c[1]][c[2]][c[3]]) - bisect.bisect_left(score[c[0]][c[1]][c[2]][c[3]], s))
        answer.append(temp)    
    
    
    return answer