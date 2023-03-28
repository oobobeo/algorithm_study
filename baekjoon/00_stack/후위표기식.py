
# 1918

'''
<풀이>
1. eq에 '()' 추가
문제가 말한데로 ()를 연산자 우선순위에 맞게 eq에 넣어줄 것이다.
+-는 일단 무시하고, */ 에 대해서만 넣어준다.
lbias,l을 이용해 '('가 들어갈 idx, rbias,r을 이용해 ')'가 들어갈 idx를 정해 주었다.
2. result 만들기
eq를 왼쪽부터 처리했다.
stack에 (operator, bias)들을 넣는 형식을 사용했다.
curr 이 
    '('면 bias += 1
    ')'면 bias -= 1, stack에서 operator의 bias가 현재bias보다 높거나 같을 때 까지 pop하여 result에 append해주었다.
    '*/+-'는 stack에 (operator, bias)로 쌓아줬다.
    isalpha()면 result에 append, '+-'에 대해 추가적으로 처리를 해줘야된다.
        해당 연산자가 나왔을 때, bias가 같으면, 달라질때까지 stack.pop() 해 result에 append해주었다.
'''
'''
문제점

다른 풀이들 보니까 문제에서 시킨대로 '()'추가 안하고 걍 후위표위식 어떻게 변환하는지 외워서 푼거 같다.
훨씬 깔끔하게 풀린다.
<다른 풀이>
stack사용
'(': stack.append
'-+': stack 이 비거나 stack[-1]!='(' 이면: result <- stack.pop(); stack.append(현재)
'*/': stack 이 비거나 stack[-1]=='*/' 이면: result <- stack.pop(); stack.append(현재) # '*/ 가 +- 보다 우위'
')':  stack 이 비거나 stack[-1]!='(' 이면: result <- stack.pop(); stack.pop()
'alpha': result.append(현재)

eq다 돌렸으면, stack에 남은것들 다 pop해서 result에 append
'''


eq = list(input())

i = 0
while i < len(eq):
    if eq[i] not in ['*','/']:
        i += 1
        continue
    l = i-1
    r = i+1
    # check left
    lbias = 0
    while True:
        if l == 0:
            break
        elif eq[l] == ')': 
            lbias += 1
            l -= 1
            continue
        elif eq[l] == '(': 
            lbias -= 1
            if lbias == 0:
                break
            l -= 1
            continue
        elif eq[l] in ['*','/','+','-']:
            l -= 1
            continue
        else:
            if lbias == 0:
                break
            l -= 1

    # check right
    rbias = 0
    while True:
        if r == len(eq)-1:
            break
        elif eq[r] == ')': 
            rbias += 1
            if rbias == 0:
                break
            r += 1
            continue
        elif eq[r] == '(': 
            rbias -= 1
            r += 1
            continue
        elif eq[r] in ['*','/','+','-']:
            r += 1
            continue
        else:
            if rbias == 0:
                break
            r += 1

    # update eq
    if r == len(eq) -1 :
        eq = eq[:l] + ['('] + eq[l:] + [')']
    else:
        eq = eq[:l] + ['('] + eq[l:r+1] + [')'] + eq[r+1:]
    i += 2


# print(''.join(eq))


# formulate result
# track (x,bias)
result = []
stack = []
bias = 0
for x in eq:
    if x == '(':
        bias += 1
    elif x == ')':
        bias -= 1
        while stack:
            if stack[-1][1] >= bias:
                result.append(stack.pop()[0])
            else:
                break
        # if bias == 0:
        #     result = result + stack[::-1]
        #     stack.clear()
    elif x in ['*','/','+','-']:
        stack.append((x,bias))
    else:
        result.append(x)
        if stack and stack[-1][0] in ['+','-'] and stack[-1][1] == bias:
            result.append(stack.pop()[0])

# print(result)
# print(stack)
while stack:
    if len(stack[-1]) == 1:
        result.append(stack.pop())
    else:
        result.append(stack.pop()[0])

print(''.join(result))











