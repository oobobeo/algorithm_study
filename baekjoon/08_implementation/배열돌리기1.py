# 16926

N,M,R = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(input().split()))


def rotate():
    # init
    x,y = 0,0
    x_len,y_len = N,M
    
    # main loop (outer layer -> inner layer)
    layer = 0
    while x_len >= 2 and y_len >= 2:
        left_corner = arr[layer][layer]
        for j in range(layer, y_len-1+layer):
            arr[layer][j] = arr[layer][j+1]
            
        for i in range(layer, x_len-1+layer):
            arr[i][y_len-1+layer] = arr[i+1][y_len-1+layer]
            
        for j in range(y_len-1+layer, layer, -1):
            arr[layer+x_len-1][j] = arr[layer+x_len-1][j-1]
            
        for i in range(x_len-1+layer, layer, -1):
            arr[i][layer] = arr[i-1][layer]
            
        arr[layer+1][layer] = left_corner
        x_len -= 2
        y_len -= 2
        layer += 1
        # break


for _ in range(R):
    rotate()

for l in arr:
    print(*l)
