def solution(board, moves):
    answer = 0
    r_len = len(board)
    
    def pick(n):
        for i in range(r_len):
            if board[i][n] != 0:
                picked = board[i][n]
                board[i][n] = 0
                return picked
        return None
    
    stack = []
    ans = 0
    for move in moves:
        picked = pick(move-1)
        if picked == None: continue
        if len(stack) > 0:
            cur_top = stack.pop()
            if picked == cur_top:
                ans += 2
                continue
            else:
                stack.append(cur_top)
                stack.append(picked)
        else:
            stack.append(picked)
                
    # print(stack)
    return ans
    