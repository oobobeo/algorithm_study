# input -> sys.stdin.readline
# for faster user input read


import sys

stack = []
iter_length = int(sys.stdin.readline())
for _ in range(iter_length):
    cmd = sys.stdin.readline().split()
    if len(cmd) >= 2: # push x
        n = cmd[1]
        stack.append(n)
    else: # else
        if cmd[0] == 'top':
            print(stack[-1]) if stack else print(-1)
        elif cmd[0] == 'empty':
            print(0) if stack else print(1)
        elif cmd[0] == 'size':
            print(len(stack))
        else: # pop
            if stack:
                print(stack.pop())
            else:
                print(-1)



