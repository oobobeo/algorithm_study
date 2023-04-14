# 21275







A,B = input().split()

count_a = 0
convA = [-1]*37
for i in range(2,37):
    try:
        convA[i] = temp = int(A,i)
        count_a += 1
    except Exception as e:
        pass

convB = [-1]*37
count_b = 0
for i in range(2,37):
    try:
        convB[i] = temp = int(B,i)
        count_b += 1
    except Exception as e:
        pass
    
if count_a == 0 or count_b == 0:
    print("Impossible")
else:
    match_a = []
    match_b = []
    for i in range(2,37):
        if convA[i] in convB and convA[i] != -1:
            match_a.append(i)
    for i in range(2,37):
        if convB[i] in convA and convB[i] != -1:
            match_b.append(i)
    # print(match_a, match_b)
    if len(match_a) == 1 and len(match_b) == 1:
        if match_a[0] == match_b[0]:
            print("Impossible")
            exit(0)
        if convA[match_a[0]] >= 2**63:
            print("Impossible")
            exit(0)
        print(convA[match_a[0]], match_a[0], match_b[0])
    elif len(match_a) == 0 or len(match_b) == 0:
        print("Impossible")
    else:
        for aa in match_a:
            if convA[aa] >= 2**63:
                print("Impossible")
                exit(0)
        print("Multiple")






