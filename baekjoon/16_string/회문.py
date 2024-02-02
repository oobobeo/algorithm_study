# 17609

T = int(input())
'''
ayxybyxa
axybyxya
어려웠던 부분: 한쪽 스킵 했을때는 안되고, 한쪽 스킵 했을 때는 되는 상황이 있었음.
'''
def get_score(word,i,j):
    while i<j:
        if word[i] == word[j]:
            i += 1
            j -= 1
        else:
            return 2
    return 1
    


ans = []
for _ in range(T):
    word = input().strip()
    i = 0
    j = len(word)-1
    score = 0
    s1 = s2 = 2
    
    # if len(word) % 2 == 0: # even
    while i<j:
        if word[i] == word[j]:
            i += 1
            j -= 1
        else:
            # left offset
            if word[i+1] == word[j]:
                score += 1
                s1 = get_score(word,i+1,j)
            # right offset
            if word[i] == word[j-1]:
                score += 1
                s2 = get_score(word,i,j-1)
            score = min(s1,s2)
            break
    ans.append(score)

for a in ans:
    print(a)
