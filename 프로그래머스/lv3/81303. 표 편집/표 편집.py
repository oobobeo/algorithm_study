def solution(N, k, cmd):
    arr = [1]*N
    nxt = [i+1 for i in range(N)]    # [1, N-1]
    nxt[N-1] = -1
    prv = [i for i in range(-1,N-1)] # [-1,N-2]
    hist = []
    cur = k
    # old_p = old_n = -1
    for eq in cmd:
        if eq == 'C':
            arr[cur] = 0
            p = old_p = prv[cur]
            n = old_n = nxt[cur]
            hist.append((cur,old_p,old_n))
            if n == -1 and p != -1: # deleted last existing element
                nxt[p] = -1
            elif n != -1 and p == -1: # deleted first existing element
                prv[n] = -1
            elif n == -1 and p == -1: # deleted last existing element
                pass
            else: # normal case
                prv[n] = p
                nxt[p] = n
            prv[cur] = nxt[cur] = -1
            if n == -1:
                cur = p
            else:
                cur = n
        elif eq == 'Z':
            z,old_p,old_n = hist.pop()
            arr[z] = 1
            # p = z-1
            # n = z+1
            # while p >= 0:
            #     if arr[p] == 1:
            #         break
            #     p -= 1
            # while n <= N-1:
            #     if arr[n] == 1:
            #         break
            #     n += 1
            if old_n != -1:
                nxt[z] = old_n
                prv[old_n] = z
            if old_p != -1:
                nxt[old_p] = z
                prv[z] = old_p
            
        elif eq[0] == 'U':
            _, i = eq.split()
            for _ in range(int(i)):
                cur = prv[cur]
        else: # "D X"
            _, i = eq.split()
            for _ in range(int(i)):
                cur = nxt[cur]
        # print(eq,'\t',arr,cur)
        # print('\t',prv)
        # print('\t',nxt)
        # print('----')
        # print(arr)
    ans = ['O' if x == 1 else 'X' for x in arr]
    return ''.join(ans)
    