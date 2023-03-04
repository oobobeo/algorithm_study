# 1874

n = int(input())
stack = []
eq = []
counter = 1
impossible_flag = 0
for _ in range(n):
    target = int(input())

    # impossible situations
    if target < counter:
        if stack:
            if stack[-1] != target:
                impossible_flag = 1
                break
    
    # solution guaranteed
    if target >= counter:
        while True:
            if target == counter:
                eq.append('+')
                eq.append('-')
                counter += 1
                break
            else:
                eq.append('+')
                stack.append(counter)
                counter += 1
    else: # in stack
        stack.pop()
        eq.append('-')




if impossible_flag:
    # print(eq)
    # print(stack)
    # print(counter)
    print("NO")
else:
    print("\n".join(eq))



