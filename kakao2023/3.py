def solution(users, emoticons):
    
    # user:      [(disc, price), ..]
    # emoticons: [cost, ..]
    
    
    # 1. 가입자 최대 늘리기
    # 2. 판매액 최대 늘리기
    # n명에게, m개 할인 판매 (10,20,30,40 %)
    
    # user:
    # 일정 % 이상 할인     -> 다 삼
    # 구매 비용합 > 일정 값 -> 구매 모두 취소, 이모티콘플러스 가입
    
    from itertools import product
    answer = []
    
    N = len(users)
    M = len(emoticons)
    
    # [10,10,30,40,30]: len=M for all possible cases
    discounts = [10,20,30,40]
    total = []
    for comb in product(discounts, repeat=M):
        comb_cost = 0
        emo_plus_count = 0
        
        for user in users:
            user_cost = 0
            for i,c in enumerate(comb):
                if c >= user[0]:
                    user_cost += emoticons[i]*(100-c)/100
            if user_cost < user[1]:
                comb_cost += user_cost
            else:
                emo_plus_count += 1
        total.append((emo_plus_count, comb_cost))
    
    # print(len(total))
    return sorted(total, reverse=True)[0]

print(solution(	[[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))
