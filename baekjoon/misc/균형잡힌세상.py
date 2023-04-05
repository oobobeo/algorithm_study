# 4949

import sys

while True:
    line = sys.stdin.readline().rstrip()
    if line == '.':
        break
    
    stack = []
    no_flag = 0
    for x in line:
        if x == '.':
            if len(stack) > 0 or no_flag:
                print("no")
            else:
                print("yes")
        elif x == '(':
            stack.append(x)
        elif x == ')':
            if not stack:
                no_flag = 1
                break
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    no_flag = 1
                    break
        elif x == '[':
            stack.append(x)
        elif x == ']':
            if not stack:
                no_flag = 1
                break
            else:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    no_flag = 1
                    break
    if no_flag:
        print("no")



























