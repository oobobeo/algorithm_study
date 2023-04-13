# 2960

N,K = map(int, input().split())


nums = [1]*(N+1)
i = 2
count = 0
while True:
    j = i
    while j <= N:
        if nums[j] == 1:
            nums[j] = 0
            count += 1
            if count == K:
                print(j)
                exit(0)
        j += i
    i += 1
