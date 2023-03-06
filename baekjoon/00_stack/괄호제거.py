# 2800
from copy import deepcopy

# has to zfill to keep the 0's in the front of the binary number


# '+', '*', '-', '/', '(', ')'
eq = input()

parans = [
[],[],[],[],[],
[],[],[],[],[],
]
stack = [] # [index, ..]
for i,x in enumerate(eq):
    if x == '(':
        stack.append(i) 
    elif x == ')':
        for l in parans:
            if len(l)>0: continue
            else:
                # print(stack)
                l.append(stack.pop())
                l.append(i)
                break
    else: 
        pass

# print(f"parans: {parans}")

# set up mask
# mask = 0b110
num_of_parans_pair = 0
for v in parans:
    if v:
        num_of_parans_pair += 1
mask = '1'*num_of_parans_pair
mask = int(mask, 2) - 0b1

# print(f"mask: {mask}")

# handle eq
exclude = set()
result = dict()
for _ in range(2**num_of_parans_pair - 1):
    exclude = set()


    # print(f"_mask: {mask}")
    mask_list = list( bin(mask)[2:].zfill(num_of_parans_pair) )
    # inverse mask_list
    mask_list = ['0' if int(x) else '1' for x in mask_list]
    # print(f"_:{_}, mask_list:{mask_list}")

    for i,x in enumerate(mask_list):
        if x == '1':
            exclude.add(parans[i][0])
            exclude.add(parans[i][1])
    
    # eq에서 exclude 빼고 출력
    temp = []
    for i,v in enumerate(eq):
        if i in exclude:
            continue
        else:
            temp.append(v)
    result[''.join(temp)] = 0

    mask -= 0b1 # casted to binary

for k in sorted(result.keys()):
    print(k)
