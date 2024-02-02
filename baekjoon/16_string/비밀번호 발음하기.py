# 4659

accept = "is acceptable."
deny   = "is not acceptable."
ans = []

vowel = ["a","e","i","o","u"]
rest  = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

while word := input().strip():
    if word == "end":
        break
    # print(0)
    # 1
    flag = 0
    for x in "aeiou":
        if x in word:
            flag = 1
            break
    if not flag:
        ans.append((word, deny))
        continue
    # print(1)
    # 2
    # vowel = 1, not = 0
    count = 1
    prv = (word[0] in vowel)
    flag = 0
    for x in word[1:]:
        if x in vowel: # cur = vowel
            if prv:
                count += 1
            else:
                count = 1
                prv = 1
        else: # cur = not
            if prv:
                count = 1
                prv = 0
            else:
                count += 1
        if count >= 3:
            ans.append((word, deny))
            flag = 1
            break
    if flag:
        continue
    # print(2)
    # 3
    prv = word[0]
    flag = 0
    for x in word[1:]:
        if prv == x and x not in "eo":
            flag = 1
            ans.append((word,deny))
            break
        prv = x
    if flag:
        continue
    # print(3)
    # acceptable
    ans.append((word, accept))

for a in ans:
    print("<",a[0],"> ",a[1],sep='')








