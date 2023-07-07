import bisect
def solution(stones, k):
    def _validate(l):
        d = 0
        for s in stones:
            if s - l > 0:
                d = 0
            else:
                d += 1
                if d >= k:
                    return False
        return True
    
    st = 0
    en = 200_000_000
    while st < en and (en-st) > 1:
        mid = (st+en) // 2
        if _validate(mid):
            st = mid
        else:
            en = mid
        # print(st,mid,en)
    
    # print(st)
    return st+1