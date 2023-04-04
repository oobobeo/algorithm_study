# 21942


'''
datetime 썻더니 느려서 노가다로 구현했다.


record에서 사용하면 없애줘야 한다..

등록된 time 이 0이면,
if record[name].get(gear) 했을때 false 판정이 난다..
'''


import sys
# from datetime import datetime, timedelta

N,L,F = input().split(' ')
N,F = map(int, (N,F))

d,t = L.split('/')
h,m = t.split(':')
d,h,m = map(int, (d,h,m))
dur = d*24*60 + h*60 + m


def datetime_to_minutes(datetime_string):

    yMd,hm = datetime_string.split(' ')
    y,M,d = map(int, yMd.split('-'))
    h,m = map(int, hm.split(':'))
    result = (d-1)*24*60 + h*60 + m

    if M == 2:
        result += 24*60*31
    elif M == 3:
        result += 24*60*59
    elif M == 4:
        result += 24*60*90
    elif M == 5:
        result += 24*60*120
    elif M == 6:
        result += 24*60*151
    elif M == 7:
        result += 24*60*181
    elif M == 8:
        result += 24*60*212
    elif M == 9:
        result += 24*60*243
    elif M == 10:
        result += 24*60*273
    elif M == 11:
        result += 24*60*304
    elif M == 12:
        result += 24*60*334

    return result
    
fee = {} # name: fee
record = {} # name: {gear: t}
for _ in range(N):
    line = sys.stdin.readline().strip()
    t = datetime_to_minutes(line[:16])
    line = line.split(' ')
    gear, name = line[2:]


    dt = 0
    if name in record: # old name
        if gear in record[name]: # returning gear
            if t > record[name][gear] + dur:
                dt = t - record[name][gear] - dur
            record[name].pop(gear)
        else: # new gear
            record[name][gear] = t
    else: # new name
        record[name] = {gear: t}

    if dt:
        if name in fee:
            fee[name] += dt*F
        else:
            fee[name] = dt*F

if fee:
    names = sorted(fee.keys())
    for name in names:
        print(name, int(fee[name]))
else:
    print(-1)





