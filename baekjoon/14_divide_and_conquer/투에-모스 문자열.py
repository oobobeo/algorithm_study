# 18222

'''
2**(step-1) < k <= 2**(step) 인 k 를 구하는 while loop 만들기가 힘들었다
차근차근 재활을 하자

'''

orig = [0,1,1,0]
k = int(input())
inv = 0
step = 0
while 2**(step) < k:
    step += 1
   

while k > 2**2:
    if k > 2**(step-1) + 2**(step-2):
        inv += 1
        k -= 2**(step-2)
    k -= 2**(step-2)
    step -= 1
print(orig[k-1]^(inv%2))
