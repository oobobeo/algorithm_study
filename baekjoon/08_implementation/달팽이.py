# 1913

N = int(input())
K = int(input())



# 1 1 2 2 3 3 4 4 5
counter = 1
direc = [(-1,0), (0,1), (1,0), (0,-1)]
i = j = i_ = j_ = N//2
arr = [[0]*N for _ in range(N)]
arr[i][j] = 1
# phase = 0
# dist = []
# for i in range(N*2):
#     dist.append(i+1)
#     dist.append(i+1)

done = False
counter = 1
for p in range(N*2):
    phase = p//2
    d = phase + 1
    way = direc[p%4]
    for k in range(d):
        i += way[0]
        j += way[1]
        # print(i,j)
        counter += 1
        if counter > N**2:
            done = True
            break
        arr[i][j] = counter
        if K == counter:
            i_,j_ = i,j
    if done:
        break
        

for l in arr:
    print(*l)
print(i_+1,j_+1)








