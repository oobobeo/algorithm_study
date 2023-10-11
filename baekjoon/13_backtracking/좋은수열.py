# 2661

N = int(input())

arr = [1]

def valid():
    # print('valid', arr)
    for l in range(1, len(arr)//2 + 1):
        # print('l',l)
            
        flag = True
        for i in range(0,len(arr)-l*2+1):
            # print('i',i)
            # # print('>', arr[i], arr[i+l])
            # print(arr,l,i)
            # print('>', arr[i:i+l], arr[i+l:i+2*l])
            if arr[i:i+l] == arr[i+l:i+2*l]:
                flag = False
                return False
    return True


def solve(idx):
    if idx == N:
        print(''.join(list(map(str, arr))))
        exit(0)
    
    for n in [1,2,3]:
        arr.append(n)
        if valid():
            solve(idx+1)
        arr.pop()
        
solve(1)
