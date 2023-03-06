# 10799


eq = list(input())


# () -> 'x'
temp = [eq[0]]
prev = None
for curr in eq[1:]:
    prev = temp.pop()
    if prev == '(' and curr == ')':
        temp.append('x')
    else:
        temp.append(prev)
        temp.append(curr)
eq = temp

# print(''.join(temp))

# process
counter = 0
level = 0
for curr in eq:
    if curr == 'x':
        counter += level
    elif curr == '(':
        level += 1
    else: # ')'
        counter += 1
        level -= 1

print(counter)
