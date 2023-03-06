# 2504


eq = list(input())

prev_eq = None
while len(eq) >= 2:
    prev_eq = eq

    # print(eq)
    # () -> 2, [] -> 3
    temp = [eq[0]]
    prev = None
    for curr in eq[1:]:
        prev = temp.pop()
        if prev == '(' and curr == ')':
            temp.append('2')
        elif prev == '[' and curr == ']':
            temp.append('3')
        else:
            temp.append(prev)
            temp.append(curr)
    eq = temp
    # print(eq)

    # end of process
    if len(eq) == 1:
        break

    # xy -> x+y
    temp = [eq[0]]
    prev = None
    for curr in eq[1:]:
        prev = temp.pop()
        if prev.isdigit() and curr.isdigit():
            temp.append( str(int(prev)+int(curr)) )
        else:
            temp.append(prev)
            temp.append(curr)
    eq = temp
    # print(eq)

    # end of process
    if len(eq) == 1:
        break

    # (x), [x] : prev1,prev2,curr
    if len(eq) >= 3:
        # print(eq)
        temp = [eq[0],eq[1]]
        prev = None
        for curr in eq[2:]:
            if len(temp) <= 1:
                temp.append(curr)
                continue
            prev2 = temp.pop()
            prev1 = temp.pop()
            if prev2.isdigit() and prev1 == '(' and curr == ')':
                temp.append(str(int(prev2) * 2))
            elif prev2.isdigit() and prev1 == '[' and curr == ']':
                temp.append(str(int(prev2) * 3))
            else:
                temp.append(prev1)
                temp.append(prev2)
                temp.append(curr)
        eq = temp
        # print(eq)
        if len(eq) == 1:
            break

    
    # check if no progression is taking place
    if prev_eq == eq:
        eq = [0]
        break
    

# print(''.join(temp))
# ex) '['
if eq[0] not in {'(',')','[',']'}:
    print(eq[0])
else:
    print(0)
