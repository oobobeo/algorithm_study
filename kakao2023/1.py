def solution(today, terms, privacies):
    answer = []
    
    # today: YYYY.MM.DD
    # terms: "type range", "A~Z 1~100"
    # privacies:
    # privacies[i]: i+1의 "start type", start: YYYY.MM.DD
    
    # today
    Y,M,D = map(int, today.split("."))
    TIME = Y*12*28 + (M-1)*28 + D
    
    terms2range = {}
    for item in terms:
        a,b = item.split()
        terms2range[a] = int(b)
    
    for i,p in enumerate(privacies):
        start, type = p.split()
        year, month, day = map(int, start.split("."))
        month += terms2range[type]
        cur_time = year*12*28 + (month-1)*28 + day
        
        if TIME >= cur_time:
            answer.append(i+1)
    
    
    
    return sorted(answer)






