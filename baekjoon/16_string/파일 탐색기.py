# 20210

import functools

"""
natural sort
"""

def alpha_p(x):
    # A:65 Z:90
    # a:97 z:122
    if x.islower():
        return (ord(x)-97)*2 + 1
    else:
        return (ord(x)-65)*2 

# a faster  -> -1
# same      -> 0
# b faster  -> 1
def alpha_comp(a, b):
    if a == b:
        return 0
    L = min(len(a), len(b))
    i = 0
    while i < L:
        if alpha_p(a[i]) < alpha_p(b[i]):
            return -1
        elif alpha_p(a[i]) > alpha_p(b[i]):
            return 1
        else:
            i += 1
    # has same prefix
    if len(a) < len(b):
        return -1
    else:
        return 1
    
def num_comp(a, b):
    if int(a) == int(b):
        a0 = len(a) - len(str(int(a)))
        b0 = len(b) - len(str(int(b)))
        if a0 < b0:
            return -1
        elif a0 > b0:
            return 1
        elif a0 == b0:
            return 0
        
    elif int(a) < int(b):
        return -1
    elif int(a) > int(b):
        return 1

def split(word):
    ret = []
    prv = word[0]
    prv_s = word[0].isnumeric()
    for x in word[1:]:
        if x.isnumeric(): # cur=num
            if prv_s: # num->num
                prv += x
            else: # alpha->num
                ret.append(prv)
                prv = x
                prv_s = True
        else: # cur=alpha
            if prv_s: # num->alpha
                ret.append(prv)
                prv = x
                prv_s = False
            else: # alpha->alpha
                prv += x
    if prv:
        ret.append(prv)
    return ret

def comp(a, b):
    al = split(a)
    bl = split(b)
    # print(al,bl)
    
    L = min(len(al), len(bl))
    i = 0
    while i < L:
        # print('i',i)
        if al[i].isnumeric() and bl[i].isnumeric():
            cc = num_comp(al[i], bl[i]) 
            if cc < 0:
                return -1
            elif cc > 0:
                return 1
            elif cc == 0:
                i += 1
        elif al[i].isnumeric() and not bl[i].isnumeric():
            return -1
        elif not al[i].isnumeric() and bl[i].isnumeric():
            return 1
        elif not al[i].isnumeric() and not bl[i].isnumeric():
            # print('alpha vs alpha')
            cc = alpha_comp(al[i], bl[i]) 
            if cc < 0:
                # print('-1')
                return -1
            elif cc > 0:
                # print('1')
                return 1
            elif cc == 0:
                # print('0')
                i += 1
                
    # a,b has same prefix
    if len(al) < len(bl):
        return -1
    elif len(al) < len(bl):
        return 1
    else:
        return 0

# main
N = int(input())
words = []
for _ in range(N):
    words.append(input().strip())

words.sort(key=functools.cmp_to_key(comp))
for w in words:
    print(w)


