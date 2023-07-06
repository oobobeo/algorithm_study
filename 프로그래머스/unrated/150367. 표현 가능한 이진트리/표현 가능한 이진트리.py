from itertools import product
def solution(numbers):
    global arr, answer
    answer = []
    # l0,l1
    arr = [[0],[1]]
    # l2
    for i in range(4):
        temp = list(product([0]+arr[i+1],repeat=2))
        li = []
        mid = 2 << (2**(i+1) -2)
        print("mid",mid)
        for a,b in temp:
            li.append((a<<(2**(i+1))) + mid + b)
        arr.append(li)
        # break
    l5 = set([])
    for l in arr:
        l5.update(l)
    print(max(l5))
        
    def validate(num):
        global answer
        if num < (2**31):
            if num in l5:
                answer.append(1)
                return
            else:
                answer.append(0)
                return
        else: # num >= 2**32
            num -= 2**31
            left = num >> 32
            right = num - (left<<32)
            # print(num,left,right)
            if left in l5 and right in l5:
                answer.append(1)
            else:
                answer.append(0)
            
    for nn in numbers:
        validate(nn)
    return answer