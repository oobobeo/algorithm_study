# 후위 표기식2


stack = []

iter_len = int(input())

eq = list(input())

# alphabet -> number
for i in range(iter_len):
    letter = chr(i+65)
    number = input()
    eq = [(number if x == letter else x) for x in eq]

# process eq
stack = []
eq.reverse()
while eq:
    head = eq.pop()
    if head.isdigit():
        stack.append(head)
        continue
    else:
        a = stack.pop()
        b = stack.pop()
        temp = str(eval(''.join([b,head,a])))
        stack.append(temp)

print(f"{float(stack[0]):.2f}")

