# 3980

N = int(input())

hist = [0]*11
check = [0]*11
score = 0
max_score = 0
def dfs(idx,ith):
    global score, max_score, check
    if idx == 11:
        max_score = max(max_score, score)
        return
    else:
        for i in range(11):
            val = arr[idx][i]
            if val != 0 and hist[i] == 0:
                score += val
                hist[i] = 1
                dfs(idx+1, 0)
                hist[i] = 0
                score -= val
                
        
        # dfs(idx, ith+1)
    

for _ in range(N):
    arr = []
    for _ in range(11):
        arr.append(list(map(int, input().split())))
    for _ in range(11):
        score = max_score = 0
        dfs(0,0)
    print(max_score)
