# 1541


eq_ = input()
eq = []
num_st = -1
for i in range(len(eq_)):
    if eq_[i] in ['-','+']:
        if num_st != -1:
            eq.append(int(eq_[num_st:i]))
            num_st = -1
        eq.append(eq_[i])
    else:
        if num_st == -1:
            num_st = i
        if i == len(eq_)-1:
            eq.append(int(eq_[num_st:]))

eq.reverse()
sub_flag = 0
result = eq.pop()
while eq:
    cur = eq.pop()
    if cur == '-':
        sub_flag = 1
        continue
    elif cur == '+':
        continue
    if sub_flag:
        result -= cur
    else:
        result += cur
print(result)




