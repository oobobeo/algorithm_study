# 16719

'''
min('aab', 'aac') = 'aab' 이용함.
'''

arr = list(input())

def m2w(mask):
    result = []
    for i,m in enumerate(mask):
        if m:
            result.append(arr[i])
    return ''.join(result)

mask = [0]*len(arr)
for _ in range(len(arr)):
    cands = [] # [(word, i), ..]
    cur_word = m2w(mask)
    
    for i,m in enumerate(mask):
        if m == 0:
            cands.append((m2w(mask[:i]+[1]+mask[i+1:]), i))
    cur_word = min(cands)
    print(cur_word[0])
    mask[cur_word[1]] = 1
