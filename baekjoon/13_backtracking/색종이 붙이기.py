# 17136

board = []
for _ in range(10):
    board.append(list(map(int, input().split())))
    



'''
use bigger sticker fist
(0,0)->(0,1)->..(0,9)->(1,0)

end cond: all covered -> save num to ans candidate

1. 5붙
2. 4붙
3. 3붙
4. 2붙
5. 1붙
'''

left = [-1,5,5,5,5,5] # filler, size1, size2, size3, size4, size5
def valid(x,y,size):
    if left[size] <= 0:
        return False
    if x+size > 10 or y+size > 10:
        return False
    for i in range(size):
        for j in range(size):
            if board[x+i][y+j] == 0:
                return False
    return True

def paint(x,y,size):
    left[size] -= 1
    for i in range(size):
        for j in range(size):
            board[x+i][y+j] = 0
            
def unpaint(x,y,size):
    left[size] += 1
    for i in range(size):
        for j in range(size):
            board[x+i][y+j] = 1
            
def end_cond():
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                return False
    return True
        
ans_cand = []
num = 0
def solve():
    global num
    # print(num)
    if end_cond():
        ans_cand.append(num)
        return
    
    for i in range(10):
        for j in range(10):
            if board[i][j] == 0: continue
            for size in [5,4,3,2,1]:
                if valid(i,j,size):
                    paint(i,j,size)
                    num += 1
                    solve()
                    num -= 1
                    unpaint(i,j,size)
            return # 이거 넣어주면 엄청 시간 줄어들어서 timeout안남.
                
solve()
if ans_cand:
    print(min(ans_cand))
else:
    print(-1)
