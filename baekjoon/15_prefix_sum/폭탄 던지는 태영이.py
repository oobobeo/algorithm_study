# 20543

N,M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
ans = [[0]*(N+1) for _ in range(N+1)]

# layer 0->(N-1)/2
for l in range((N-1)//2):
    # copy outer layer
    step = l+(M-1)//2 # M=3 -> step=l+1
    outer = [[0]*(N+1) for _ in range(N+1)]
    for x in range(l,N-l):
        outer[x][l] = board[x][l]
        outer[l][x] = board[l][x]
        outer[N-1-l][x] = board[N-1-l][x]
        outer[x][N-1-l] = board[x][N-1-l]
    
    print('_'*len(outer)*3)
    print('l',l,'outer')
    for ooo in outer:
        print(ooo)
    print('^'*len(ooo)*3)
    
    # calculate ans using outer layer
    m = (M-1)//2
    for s in range(l+m,N-1-l-m):
        # print((s-m,l+m-m),)
        # lu -> ld
        ans[s][l+m] = -outer[s-m][l+m-m]
        for i in range(-m,m+1): # -m,..0,..,m
            outer[s+i][l] -= ans[s][l+m]
    for s in range(l+m+1, N-1-l-m):
        # lu -> ru
        ans[l+m][s] = -outer[l+m-m][s-m]
        for i in range(-m,m+1): # -m,..0,..,m
            outer[l][s+i] -= ans[l+m][s]
    
    for s in range(l+m+1, N-1-l-m):
        # rd -> ru
        ans[s][l+m] = -outer[s+m][l+m+m]
        for i in range(-m,m+1): # -m,..0,..,m
            outer[N-1-(s+i)][l] -= ans[N-1-s][l+m]
    for s in range(l+m+1, N-1-l-m):
        # rd -> ld
        ans[l+m][N-s] = -outer[l+m+m][N-s+m]
        for i in range(-m,m+1): # -m,..0,..,m
            outer[l][N-1-(s+i)] -= ans[l+m][N-1-s]
    
    print('l',l,'ans')
    for aaa in ans:
        print(aaa)
    print('-----------------------------')
            
    # mark edges for acc sum using outer
    edges = [[0]*(N+1) for _ in range(N+1)]
    pos_offset = [(-m,-m), (m+1,m+1)]
    neg_offset = [(-m,m+1), (m+1,-m)]
    for x in range(m+l, N-m-l):
        for i,j in pos_offset:
            edges[x+i][m+l+j] += ans[x][m+l]
        for i,j in neg_offset:
            edges[x+i][m+l+j] -= ans[x][m+l]
    for y in range(m+l+1, N-m-l):
        for i,j in pos_offset:
            edges[m+l+i][y+j] += ans[m+l][y]
        for i,j in neg_offset:
            edges[m+l+i][y+j] -= ans[m+l][y]
    for x in range(m+l+1, N-m-l):
        for i,j in pos_offset:
            edges[x+i][N-1-m-l+j] += ans[x][N-1-m-l]
        for i,j in neg_offset:
            edges[x+i][N-1-m-l+j] -= ans[x][N-1-m-l]
    for y in range(m+l+1, N-m-l-1):
        for i,j in pos_offset:
            edges[N-m-l-1+i][y+j] += ans[N-m-l-1][y]
        for i,j in neg_offset:
            edges[N-m-l-1+i][y+j] -= ans[N-m-l-1][y]
    
    # calculate damage using edges
    for i in range(N+1):
        acc = 0
        for j in range(N+1):
            acc += edges[i][j]
            edges[i][j] += acc
    for j in range(N+1):
        acc = 0
        for i in range(N+1):
            acc += edges[i][j]
            edges[i][j] += acc
    
    # update board
    for i in range(N):
        for j in range(N):
            board[i][j] -= edges[i][j]
    
    
        
# print ans
for aaa in ans[:-1]:
    print(' '.join(map(str, aaa[:-1])))
            
    







