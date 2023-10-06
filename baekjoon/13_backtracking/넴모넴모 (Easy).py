# 14712

# 멍청한풀이 (brute force, dfs, 전체 상황 완전탐색)
# 부터 생각하자!

import itertools

N,M = map(int, input().split())

# arr = [[0]*(2**N) for _ in range(2**N)]
# arr = list(itertools.product([0,1], repeat=N))

# # adjacent possibility
# table = [[0]*(2**N) for _ in range(2**N)]

# def validate(a,b):
#     for i in range(N-1):
#         if a[i] == 1 and a[i+1] == 1 and b[i] == 1 and b[i+1] == 1:
#             return 0
#     return 1

# for x in range(2**N):
#     for y in range(2**N):
#         table[x][y] = validate(arr[x],arr[y])

# # print(arr)
# # print(table)
# table_sum = [sum(table[i]) for i in range(2**N)]

# ans = 2**N
# cur_last = [1]*(2**N)
# for _ in range(M-1):
#     nxt_last = [0]*(2**N)
#     for i in range(2**N):
#         for j in range(2**N):
#             nxt_last[j] += cur_last[i]*table[i][j]
#     # print(cur_last)
#     ans = sum([cur_last[i]*table_sum[i] for i in range(2**N)])
#     cur_last = nxt_last

# print(ans)

board = [[0]*(M+1) for _ in range(N+1)]

def nxt(x,y):
    if y < M:
        return (x,y+1)
    else:
        return (x+1,1)
# dfs, but (0,0) -> (0,1) -> (1,0) -> (1,1)
ans = 0
def dfs(x,y):
    global ans
    if x > N or y > M:
        ans += 1
        return   
    
    # print(board)
    
    next_coor = nxt(x,y)
    # print(*next_coor)
    # cur x
    dfs(*next_coor)
        
    # cur o
    if board[x-1][y-1] == 1 and board[x][y-1] == 1 and board[x-1][y] == 1:
        return
    else:
        board[x][y] = 1
        dfs(*next_coor)
        board[x][y] = 0
    
dfs(1,1)
print(ans)
