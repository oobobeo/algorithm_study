import math
import requests as re
import bisect









global TOKEN
global AUTH_KEY
AUTH_KEY = ''
TOKEN = '37cdb77edefcbc5636a53d88828e5753'
URL = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'
headers = {"X-Auth-Token": TOKEN}


'''
Match       짝짓기. 턴종료. 595+1 번 실행시키면 simulation end
WaitingLine 대기 중인 유저들 정보
GameResult  이번턴에 끝난 게임 결과 정보

ChangeGrade 유저 등급 수정


'''

# 게임 시작
def start(num):
    global AUTH_KEY
    r = re.post(URL+'/start', headers=headers, data={'problem': num})
    AUTH_KEY = r.json()["auth_key"]
    # return r.json()["auth_key"]


# 현재 대기열
def waiting_line():
    global AUTH_KEY
    r = re.get(URL+'/waiting_line', headers={"Authorization": AUTH_KEY})
    return [[x['id'],x['from']] for x in r.json()["waiting_line"]]

# 이번턴 끝난 게임결과
# -> [{id, from}]
def game_result():
    global AUTH_KEY
    r = re.get(URL+'/game_result', headers={"Authorization": AUTH_KEY})
    return r.json()["game_result"]

# 모든 유저 현재 등급
def user_info():
    global AUTH_KEY
    r = re.get(URL+'/user_info', headers={"Authorization": AUTH_KEY})
    info = r.json()["user_info"]
    result = [0]*901
    for d in info:
        result[d['id']] = d['grade']
    return result


# [(id1, id2), ..] -> (status, time_step)
def match(pairs = []):
    global AUTH_KEY
    r = re.put(URL+'/match', headers={"Authorization": AUTH_KEY, "Content-Type": "application/json"}, json={'pairs': pairs})
    r = r.json()
    print(r)
    if "message" in r:
        return r
    return [r["status"], r["time"]]

# [(id,grade), ..] -> status
def change_grade(l):
    global AUTH_KEY
    payload = [{"id": x[0], "grade": x[1]} for x in l]
    r = re.put(URL+'/change_grade', headers={"Authorization": AUTH_KEY}, json={"commands": payload})
    return r.json()["status"]
    
def score():
    global AUTH_KEY
    r = re.get(URL+'/score', headers={"Authorization": AUTH_KEY})
    return r.json()

##############################################
m_count = [[0]*901 for _ in range(901)] # m_count[low][high] = match count
m_win = [[0]*901 for _ in range(901)]   # m_win[low][high]   = win   count
m_time = [[0]*901 for _ in range(901)]  # m_time[low][high]  = avg match time
grade = [0]*901                         # grade[id]          = grade of each id
global lmbda
lmbda = 1

def grade_diff(time):
    e = 0
    diff = (40+e-time)*99000/35
    return diff

# a_id < b_id
#                 id    id   1|0  int   float  2d-arr
def update_score(a_id, b_id, won, time, decay, ranks):
    global lmbda
    grade_diff_ = grade_diff(time)
    m_count[a_id][b_id] += 1
    m_win[a_id][b_id] += won
    m_time[a_id][b_id] = (m_time[a_id][b_id]*(m_count[a_id][b_id] - 1) + time) / m_count[a_id][b_id]
    old_a_g, old_b_g = grade[a_id], grade[b_id]
    # monte-carlo-esque
    
    lmbda *= decay
    a_p = m_win[a_id][b_id]/m_count[a_id][b_id]
    b_p = 1 - a_p
    if a_p == 0 or a_p == 1:
        delta = grade_diff_//2
        if won: 
            grade[a_id] = 20000 - delta
            grade[b_id] = 20000 + delta
        else:
            grade[a_id] = 20000 + delta
            grade[b_id] = 20000 - delta
        return
    
    if a_p*2 == 1: # no adjustments
        return
    elif a_p*2 < 1:
        a_target = (a_p*grade_diff_)/(1-2*a_p)
        if a_target < 0:
            return
        grade[a_id] += int((a_target - a_p)*lmbda)
        b_target = a_target + grade_diff_
        if b_target < 0:
            return
        grade[b_id] += int((b_target - a_p)*lmbda)
        grade[b_id] = b_p
    else:
        a_target = (a_p*grade_diff_)/(-1+2*a_p)
        if a_target < 0:
            return
        grade[a_id] += int((a_target - a_p)*lmbda)
        b_target = a_target - grade_diff_
        if b_target < 0:
            return
        grade[b_id] += int((b_target - a_p)*lmbda)
        grade[b_id] = b_p
        
    # sort ranks: delete [x,a_id], [x,b_id] -> insort both
    ranks.remove([old_a_g, a_id])
    ranks.remove([old_b_g, b_id])
    bisect.insort_left([grade[a_id], a_id])
    bisect.insort_left([grade[b_id], b_id])
    
        
    
    
    
    # if won == 1: # a won
    a_target = (1/a_p - grade_diff_)/2
    if a_target < 0:
        return
    grade[a_id] += int((a_target - a_p)*lmbda)
    b_target = (1-a_p)/(1-2*a_p) * grade_diff_
    if b_target < 0:
        return
    grade[b_id] += int((b_target - a_p)*lmbda)
    grade[b_id] = b_p
    # sort ranks: delete [x,a_id], [x,b_id] -> insort both
    ranks.remove([old_a_g, a_id])
    ranks.remove([old_b_g, b_id])
    bisect.insort_left([grade[a_id], a_id])
    bisect.insort_left([grade[b_id], b_id])
    
    # else:        # b won
    return grade[a_id], grade[b_id]

ranks1 = [[0,i] for i in range(1,31)]
ranks2 = [[0,i] for i in range(1,901)]
# return closest person with similar grade
def get_closest(id, waits ,ranks, cur_t):
    arr = [[grade[id_], cur_t-t, id_] for id_, t in waits if id_ != id] # grade, time_passed, id
    arr.sort()
    if grade[id] == 0: # not yet encountered
        # print('arr', arr)
        # print('aaa', [ranks[len(ranks)//2][0], 0, 0])
        k = bisect.bisect_left(arr, [ranks[len(ranks)//2][0], 0, 0])
        # print('k', k)
        return [arr[k][2], -arr[k][1]+cur_t]
    k = bisect.bisect_left(arr, [grade[id], 0, 0])
    if k == len(arr): k -= 1
    return [arr[k][2], -arr[k][1]+cur_t]

def generate_pairs(waits, ranks, cur_t, time_window):
    pairs = []
    waits.sort(key=lambda x: -x[1])
    while cur_t - waits[-1][1] >= time_window and len(waits) >= len(ranks)//3:
        id1 = waits.pop()[0]
        id2 = get_closest(id1, waits, ranks, cur_t)
        # print('id2:', id2)
        waits.remove(id2)
        pairs.append([id1,id2[0]])
    return pairs


##############################################
token = start(1)
match()
for i in range(1, 595):
    print('^^^^^^^^^^^^^^^^^^^')
    # update scores
    results = game_result()
    for result in results:
        id1 = result['win']
        id2 = result['lose']
        time = result['taken']
        a_id = min(id1,id2)
        b_id = max(id1,id2)
        won = 1 if a_id == id1 else 0
        update_score(a_id, b_id, won, time, 1, ranks1)
    
    # make matches
    waits = waiting_line()
    pairs = generate_pairs(waits, ranks1, i, 10)
    # print('waits:', waits)
    
    # print('pairs', pairs)
    # print('waits:', waits)
    print(grade)
    print('----------')
    match(pairs)
    
commands = [{"id": i+1, "grade": x} for i,x in enumerate(grade[1:])]
    
change_grade(commands)
# print(score())
match() # end
print(score())















