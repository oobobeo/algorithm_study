# 21314




eq = list(input().strip())

parsed_eq = []
temp = []
for x in eq:
    if x == 'K': # flush
        temp.append('K')
        parsed_eq.append(temp)
        temp = []
    else: # M
        temp.append('M')
if temp:
    parsed_eq.append(temp)

def parse(x):
    result = []
    # x.reverse()
    st = x.pop()
    if st == 'M':
        result.append('1')
    else: # K
        result.append('5')
    while x:
        result.append('0')
        x.pop()
    return (''.join(result))


big = []
small = []
for x in parsed_eq:
    if x[-1] == 'K':
        big.append(parse(x[:]))
    else:
        for _ in range(len(x)):
            big.append('1')
    # small
    if x[-1] == 'K' and len(x) >= 2:
        small.append(parse(x[:-1]))
        small.append('5')
    else:
        small.append(parse(x))
print(''.join(big))
print(''.join(small))





