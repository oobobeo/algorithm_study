# 1343




board = input()
result = list(board)

# fill [st,i] greedily
def fill(st,i):
    while st < i:
        if i-st >=4:
            result[st] = 'A'
            result[st+1] = 'A'
            result[st+2] = 'A'
            result[st+3] = 'A'
            st += 4
        else:
            result[st] = 'B'
            result[st+1] = 'B'
            st += 2

st = 0
conti = 0
for i in range(len(board)):
    # get conti X
    if board[i] == '.':
        # calculate for [st,i-1]
        if conti == 1:
            if (i-st)%2 == 1:
                # print(st,i)
                print(-1)
                exit(0)
            fill(st,i)
        conti = 0
    elif board[i] == 'X':
        if conti == 0:
            st = i
        conti = 1

# if input ends with 'X'
if conti:
    i = len(board)
    if (i-st)%2 == 1:
        print(-1)
        exit(0)
    fill(st,i)

print(*result,sep='')


