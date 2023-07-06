def solution(board, skill):
    r_len = len(board)
    c_len = len(board[0])
    
    arr = [[0]*(c_len+1) for _ in range(r_len+1)]
    for t,r1,c1,r2,c2,deg in skill:
        arr[r2+1][c2+1] += (2*t-3)*deg
        arr[r2+1][c1] -= (2*t-3)*deg
        arr[r1][c2+1] -= (2*t-3)*deg
        arr[r1][c1] += (2*t-3)*deg
        
    agg = [[0]*(c_len+1) for _ in range(r_len+1)]
    agg[r_len][c_len] = arr[r_len][c_len]
    for j in range(c_len-1,0,-1):
        agg[r_len][j] = agg[r_len][j+1] + arr[r_len][j]
    for i in range(r_len-1,0,-1):
        agg[i][c_len] = agg[i+1][c_len] + arr[i][c_len]
    
    for i in range(r_len-1,0,-1): 
        for j in range(c_len-1,0,-1):
            agg[i][j] = agg[i+1][j] + agg[i][j+1] - agg[i+1][j+1] + arr[i][j]

    answer = 0
    for i in range(r_len):
        for j in range(c_len):
            board[i][j] += agg[i+1][j+1]
            if board[i][j] > 0:
                answer += 1
    # print(board)
    return answer
            
            
            
            
            
            
            
            