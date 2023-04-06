# 5639

'''
class Node 만들어서 tree 구현하려는 삽질 절대 하지말자.

힌트를 보고 (st,en) 구간별 recursion으로 풀었는데 메모리 초과과 났다.
알고보니 sys.setrecursionlimit(N) 을 너무 큰 수로 하면
memory exceeded error 가 난다.

iterative하게도 풀었다.

<풀이>
받는 숫자들이 inorder여서 (root,left[],right[]) 형식으로 들어온다.
일단 숫자들을 다 받아서 tree[]에 넣어놓는다.
postorder() 는 임의의 구간 (st,en) 에 대해:
    postorder(left[])->postorder(right[])->print(root)
    해주는 함수이다.
    받은 구간 st,en에서 
    right 이 사작되는 인덱스 mid를 찾고, st,mid,en을 이용해서
    left[],right[]가 있는지 없는지 여부를 판단해준다.
임의의 구간에 대해 left->right->root 순서로 처리해주면,
전체 구간에 대해 left->right->root 순서로 처리된다.
'''

import sys

sys.setrecursionlimit(10500)

tree = []
for line in sys.stdin:
    line = line.strip()
    if not line:
        break
    tree.append(int(line))
    
# root,left,right -> left,right,root
def postorder(st, en):
    # global result
    if en < st: return
    mid = st+1
    while mid <= en and tree[mid] < tree[st]:
        mid += 1
    if st+1 <= mid-1:
        postorder(st+1, mid-1)
    if mid <= en:
        postorder(mid, en)
    print(tree[st])
    
# print(*result)
postorder(0,len(tree)-1)





# iterative 풀이

# result = []
# call_stack = [(0,len(tree)-1)]
# while call_stack:
#     line = call_stack.pop()
#     if type(line) == int:
#         result.append(line)
#         continue
#     else:
#         st,en = line
#     if en < st:
#         continue

#     mid = st+1
#     while mid <= en and tree[mid] < tree[st]:
#         mid += 1
#     if st+1 <= mid-1:
#         call_stack.append((st+1, mid-1))
#     if mid <= en:
#         call_stack.append((mid, en))
#     call_stack.append(tree[st])

# for x in result[::-1]:
#     print(x)



