# 2580

'''
10^12 정도 되나..
복잡한 케이스는 엄청 커질거 같은데
가능한 상태가 2개 이상인 보드가 있어서 인간이 푸는것 처럼 풀면 안됨
backtracking으로 bruteforce..
4.7초 평균으로 통과
'''

arr = []
for _ in range(9):
    arr.append(list(map(int, input().split())))

# backtracking 으로 완전탐색 해야됨.
def validate(r,c):
    # row
    found = [0]*10
    for j in range(9):
        found[arr[r][j]] += 1
        if found[arr[r][j]] == 2 and arr[r][j] != 0:
            return False
    # col
    found = [0]*10
    for i in range(9):
        found[arr[i][c]] += 1
        if found[arr[i][c]] == 2 and arr[i][c] != 0:
            return False
    
    # box
    if 0 <= r < 3:
        a = 0
    elif 3 <= r < 6:
        a = 3
    else:
        a = 6
    if 0 <= c < 3:
        b = 0
    elif 3 <= c < 6:
        b = 3
    else:
        b = 6
    found = [0]*10
    for i in range(3):
        for j in range(3):
            found[arr[a+i][b+j]] += 1
            if found[arr[a+i][b+j]] == 2 and arr[a+i][b+j] != 0:
                return False

    return True

blanks = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            blanks.append((i,j))

def explore(idx):
    # end cond
    if idx == len(blanks):
        for l in arr:
            print(*l)
        exit(0)
        
    x,y = blanks[idx]
    
    for n in range(9):
        arr[x][y] = n+1
        if validate(x,y):
            explore(idx+1)
        arr[x][y] = 0
        
explore(0)










# # 1. check row
# # 2. check col
# # 3. check box
# # 4. update arr

# # 9x9x10
# cands = [[[1]*10 for _ in range(9)] for _ in range(9)]
# for i in range(9):
#     for j in range(9):
#         cands[i][j][0] = 0
#         if arr[i][j] != 0:
#             cands[i][j] = [0]*10
# # print(cands)

# def check_rows():
#     for i in range(9):
#         found = [0]*10 # x,1,2,..,9
#         for x in arr[i]:
#             found[x] = 1
#         for idx,x in enumerate(found[1:]):
#             if x == 1:
#                 for j in range(9):
#                     cands[i][j][idx+1] = 0

# def check_cols():
#     for c in range(9):
#         found = [0]*10 # x,1,2,..,9
#         for r in range(9):
#             x = arr[r][c]
#             found[x] = 1
            
#         for idx,x in enumerate(found[1:]):
#             if x == 1:
#                 for r in range(9):
#                     cands[r][c][idx+1] = 0
                    
# def check_box():
#     starts = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
#     for r,c in starts:
#         found = [0]*10 # x,1,2,..,9
#         for i in range(3):
#             for j in range(3):
#                 x = arr[r+i][c+j]
#                 found[x] = 1
                
#         for idx,x in enumerate(found[1:]):    
#             if x == 1:
#                 for i in range(3):
#                     for j in range(3):
#                         cands[r+i][c+j][idx+1] = 0

# def update():
#     for i in range(9):
#         for j in range(9):
#             if sum(cands[i][j][1:]) == 1 and arr[i][j] == 0:
#                 for idx,x in enumerate(cands[i][j]):
#                     if x == 1:
#                         arr[i][j] = idx
#                         break

# for _ in range(100):
#     check_rows()
#     check_cols()
#     check_box()
#     update()
# # print()
# for l in arr:
#     print(*l)
