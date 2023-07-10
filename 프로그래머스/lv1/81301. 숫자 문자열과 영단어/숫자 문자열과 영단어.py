def solution(s):
    answer = []
    def _isnum(x):
        return x in '0123456789'
    trans = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    i = j = 0
    while j <= len(s)-1:
        if i == j:
            if _isnum(s[i]):
                answer.append(s[i])
                i += 1
                j += 1
            else:
                j += 1
        else:
            if s[i:j+1] in trans:
                answer.append(str(trans[s[i:j+1]]))
                j += 1
                i = j
            else:
                j += 1
    print(answer)
    return int(''.join(answer))
