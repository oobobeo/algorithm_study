# 11726























# (k개, 끝 작대기 ori: |,=)
# a(k,0) = a(k-1,all)
# a(k,1) = a(k-2,all)
# a(0,all) = 0
# a(1,all) = [1,0]
# a(2,all) = [1,1]
# a(3,all) = [2,1]
# a(4,all) = [3,2]
N = int(input())
# d = [[0,0] for _ in range(N+4)]
d = [0]*(N+4)
d[0] = 0
d[1] = 1
d[2] = 2
# d[3] = [2,1]
for i in range(2,N):
    # print(i)
    # print(d)
    d[i+1] = d[i] + d[i-1]
print(d[N] % 10007)


