# 13549

'''
생각보다 엄청 애먹었다
1. stack에 넣어줄때, (cur, d) 이렇게 넣어주면, d 가 최신의 dists가 아님.
    -> dists[] 로 최신의 dist들 따로 관리해주자
2. cur->cur*2 가 cost=0 이여서, cur*(2**i) 를 cur 한개 처리할때, 다 stack에 넣어줬는데
    -> stack 에 중복으로 들어가는 일이 발생한다
3. N->K (N<K) 로 가는 과정에서 N->...->K+1->K 로 가는게 가장 효율적인 방법이 있다
    -> dists[K+2] 로 잡아서 idx=K+1 까지 커버해 줘야한다.
4. 28-29 줄은 틀렸다..
    -> N=(K-1)//2 같은 경계값들을 꼼꼼히 확인해주자
'''



N,K = map(int, input().split())


if K == N:
    print(0)
elif K < N:
    print(N-K)
elif N < K:
    if K//2 <= N:
        if K % 2 == 0: # K = even
            print(min(K-N, N - K//2))
        elif K % 2 == 1:
            print(min(K-N, N - (K+1)//2 + 1))
    else:            
        L = K+1
        dists = [300000]*L
        dists[N] = 0
        stack = [N]
        while stack:
            # print(stack)
            cur = stack.pop()
            if cur-1 >= 0 and dists[cur-1] > dists[cur]+1:
                dists[cur-1] = dists[cur]+1
                stack.append(cur-1)
            if cur+1 < L and dists[cur+1] > dists[cur]+1:
                dists[cur+1] = dists[cur]+1
                stack.append(cur+1)
            if cur*2 < L and dists[cur*2] > dists[cur]:
                dists[cur*2] = dists[cur]
                stack.append(cur*2)
        # print(dists)
        print(dists[K])
            