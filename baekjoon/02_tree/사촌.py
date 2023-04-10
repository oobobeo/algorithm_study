# 9489


'''
grandparent 가 같으면 sibling.
1. parent p[] 에 각 index에 해당하는 element의 parent index 저장.
    arr의 각 element 순회하면서 prev,next 가 1차이가 나는지 비교해준다.
    1차이 이상이면 현재 부모(curr_p) 의 children 이 다 나왔고, 다음 parent handling 해준다.
    어차피 arr는 오름차순이므로, arr의 왼쪽부터가 curr_p가 된다.
2. bisect로 현재 node의 gp,p를 찾고 -> cousin range를 찾는다. O(logN)
    p[]에서 gp에 대해 bisect_left,right을 해주면
        parent가 gp인 node들의 index range를 구할수 있다. (parent의 형제들)
    parent 형제들의 가장 왼쪽의 왼쪽 자식, 가장 오른쪽의 오른쪽 자식을 구한다.
        cousin range가 구해진다.
    여기서 sibling range를 빼주어 cousin 개수를 구한다.
'''



import sys
from collections import deque
import bisect


while True:
    N,K = map(int, input().split())
    if N == 0 and K == 0: break
    arr = list(map(int, sys.stdin.readline().split()))
    p = [-1]*N
    prev = arr[0]
    curr_p = -1
    for i in range(1,N):
        curr = arr[i]
        if prev+1 < curr:
            curr_p += 1
            p[i] = curr_p
        else:
            p[i] = curr_p
        prev = curr

    # search cousin
    k = bisect.bisect_left(arr,K)
    if p[k] == -1:
        print(0)
        continue
    g = p[p[k]]
    l = bisect.bisect_left(p,g)
    r = bisect.bisect_right(p,g) - 1
    ll = bisect.bisect_left(p,l)
    rr = bisect.bisect_right(p, r)
    result = rr - ll

    # subtract siblings
    l = bisect.bisect_left(p,p[k])
    r = bisect.bisect_right(p,p[k])
    result = result - r + l
    print(result)
