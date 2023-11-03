N,M,H = map(int, input().split())

red_lines = [tuple(map(int, input().split())) for _ in range(M)]
path = [[0]*(N-1) for _ in range(H)]
for h,r in red_lines:
    path[h-1][r-1] = 1


def combinations(arr,r):
    if r == 0:
        return [[]]
    else:
        comb = []
        for i in range(len(arr)):
            for tail in combinations(arr[i+1:], r-1):
                comb.append([arr[i]]+tail)
    return comb


cache = {}
def choose(arr,num):
    # print('choose', arr, num)
    key = str(arr)+str(num)
    # print('key',key)
    if key in cache:
        # print('cache')
        # print(cache)
        return cache[key]
    else:
        # print('a')
        zero_indices = []
        for i,n in enumerate(arr):
            if n == 0:
                zero_indices.append(i)
        if num == 0:
            # print('b')
            cache[key] = [arr]
            return [arr]
        else:
            # print('c')
            possibilities = []
            # print('arr', arr)
            combs = combinations(zero_indices, num)
            # print('comb')
            # print(combs)
            for c in combs:
                temp = arr[:]
                for cc in c:
                    temp[cc] = 1
                # print('temp', temp)
                # check validity
                valid = True
                for i in range(len(temp)-1):
                    if temp[i] == 1 and temp[i+1] == 1:
                        # not valid
                        valid = False
                        break
                if valid: # and temp[-1] == 0:
                    # print('temp', temp)
                    possibilities.append(temp)
        cache[key] = possibilities
        # print('possibilities',possibilities)
        return possibilities
    
    

target = [i for i in range(N)]
cur = [i for i in range(N)]
min_len = 4
def solve(layer, used_num):
    global cur, target, min_len
    # print(layer, used_num, cur)
    if layer == H:
        if cur == target and used_num <= 3:
            min_len = min(min_len, used_num)
    else:
        for num in range(4-used_num):
            possibilities = choose(path[layer], num)
            # print('possibilities',possibilities)
            for pp in possibilities:
                cur_save = cur[:]
                temp_cur = cur
                temp_layer = path[layer][:]
                # print('pp', pp)
                # for ppp in pp:
                #     temp_layer[ppp] = 1
                for i in range(len(pp)):
                    temp_layer[i] = pp[i]
                    
                
                # print('pp',pp)
                # print('1',temp_cur)
                for idx in range(N-1):
                    if pp[idx] == 1:
                        tt = temp_cur[idx+1]
                        temp_cur[idx+1] = temp_cur[idx]
                        temp_cur[idx] = tt
                        # temp_cur[idx],temp_cur[idx+1] = temp_cur[idx+1],temp_cur[idx]
                # print('2',temp_cur)
                
                cur = temp_cur[:]
                solve(layer+1, used_num+num)
                cur = cur_save[:]
    
    
solve(0,0)
if min_len == 4:
    print(-1)
else:
    print(min_len)

# print(choose([1,0,0,1,0,1,0,0,0,0,0],2))




#### 해설 코드 ####
import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력
n, m, h = tuple(map(int, input().split()))
line = [
    [False for _ in range(n + 1)]
    for _ in range(h + 1)
]

# i번째 줄이 어디로 향하는지
# 계산하기 위해 필요한 배열입니다.
num = [0 for _ in range(n + 1)]

candidates = []

ans = INT_MAX


#i번째 줄이 전부 i번으로 가는지 확인합니다.
def possible():
    # 유실 선끼리 이어져있는지 확인하고
    # 그런 경우에는 불가능하다 판단합니다.
    if any([
        line[a][b] and line[a][b - 1]
        for a in range(1, h + 1)
        for b in range(2, n)
    ]):
        return False
    
    # 직접 어느 위치로 이동하는지를
    # 계산하기 위해 초기값을 설정해줍니다.
    for i in range(1, n + 1):
        num[i] = i
	
    # 유실 선이 있는 경우
    # 해당 위치에 있는 고객의 번호를 서로 교환합니다.
    for a in range(1, h + 1):
        for b in range(1, n):
            if line[a][b]:
                num[b], num[b + 1] = num[b + 1], num[b]
    
    # 전부 자기 자신으로 내려오는지 확인합니다.
    if any([
        num[i] != i
        for i in range(1, n + 1)
    ]):
        return False
    
    return True


def find_min(curr_idx, cnt):
    global ans
    
    # 추가한 유실선의 수가
    # 이미 지금까지 구한 답보다 좋아질 수 없다면
    # 퇴각합니다.
    if cnt >= ans:
        return
    
    # 가능한 조합이라면, 답을 갱신합니다.
    if possible():
        ans = min(ans, cnt)
    
    # 이미 3개를 뽑았거나, 더 이상 뽑을 게 없다면
    # 퇴각합니다.
    if cnt == 3 or curr_idx == len(candidates):
        return

    # curr_idx 번째 유실선은 추가하지 않았을 경우
    find_min(curr_idx + 1, cnt)
    
    # curr_idx 번째 유실선을 추가헀을 경우
    # 해당 위치에 유실선을 추가해줍니다.
    a, b = candidates[curr_idx]
    line[a][b] = True
    find_min(curr_idx + 1, cnt + 1)
    line[a][b] = False

    
for _ in range(m):
    a, b = tuple(map(int, input().split()))
    line[a][b] = True
    
# 선을 놓을 수 있는 목록 생성
candidates = [
    (i, j)
    for i in range(1, h + 1)
    for j in range(1, n)
    if not line[i][j]
]

find_min(0, 0)

if ans == INT_MAX:
    ans = -1

# 출력:
print(ans)