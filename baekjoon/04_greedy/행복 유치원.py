# 13164

'''
arr[-1]-arr[0]-sum(max_diff) 는 틀리고
ans, sum(diff_sorted[:N-K]) 는 맞는 이유를 모르겠다.

예제는 다 맞음.


'''




import sys

N,K = map(int, input().split())

arr = list(map(int, sys.stdin.readline().split()))
arr = sorted(arr)
diff = []
for i in range(1,len(arr)):
    diff.append(arr[i]-arr[i-1])
diff_sorted = sorted(diff)
max_diff = diff_sorted[-K+1:]


# print(arr[-1]-arr[0]-sum(max_diff))
ans = arr[-1]-arr[0]
for i in range(N-2,N-K-1,-1):
    ans -= diff_sorted[i]
print(ans)
print(sum(diff_sorted[:N-K]))









