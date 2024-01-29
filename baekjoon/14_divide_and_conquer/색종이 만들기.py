# 2630

'''
4개의 근접하는 element가 같음 -> 0인case, else 이렇게 나눴는데, 이러면 -1,1 인경우가 같이 묶어지는 것을 생각을 못해서 헤맸다..
교훈) 역시 else보다는 elif로 분기를 확실히 타주는게 실수가 적어질 것.
'''

# element = 0,1,-1(mixed)
# iterative NxN -> (N/2)x(N/2) ..-> 2x2
# count (number of -1) + 1(if board is filled w/ same val)

N = int(input())
board = []
for _ in range(N):
    temp = list(map(int, input().split()))
    board.append(temp)


zero_count = 0
one_count  = 0

nxt_l = N//2
while nxt_l >= 1:
    nb = [[-1]*nxt_l for _ in range(nxt_l)]
    
    for i in range(nxt_l):
        for j in range(nxt_l):
            if board[2*i][2*j] == board[2*i][2*j+1] == board[2*i+1][2*j] == board[2*i+1][2*j+1]:
                if board[2*i][2*j] == 0:
                    nb[i][j] = 0
                elif board[2*i][2*j] == 1: # board에서 [-1,0,1] 쓰기 때문에, 그냥 else로 하면 안됨.
                    nb[i][j] = 1
            else:
                for x in range(2):
                    for y in range(2):
                        if board[2*i+x][2*j+y] == 0:
                            zero_count += 1
                        elif board[2*i+x][2*j+y] == 1:
                            one_count += 1
                            
    if nxt_l != 1:
        board = nb
    nxt_l //= 2
if board[0][1] == board[0][0] == board[1][0] == board[1][1]:
    if board[0][0] == 0:
        zero_count += 1
    elif board[0][0] == 1:
        one_count += 1

print(zero_count)
print(one_count)
