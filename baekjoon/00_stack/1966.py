# 프린터 큐

iter_num = int(input())
for _ in range(iter_num):
    # dics = {importance: [idx,..], .. }
    dics = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], }

    n,m = list(map(int, input().split())) # 문서 개수, 찾고싶은 문서 index
    docs = list(map(int, input().split())) # 문서 리스트

    # docs -> dics 
    for idx in range(len(docs)):
        dics[docs[idx]].append(idx)
    # print(dics)

    count = 0
    # loop through dics[ >importance] while keeping eye on index
    target_importance = docs[m]
    head_idx = 0 # index of the head after all the documents of the certain importance are handled
    for importance in [9,8,7,6,5,4,3,2,1]:
        # print(f"imp: {importance} head_idx: {head_idx}")
        if len(dics[importance]) == 0: continue;
        if target_importance >= importance: break;

        head_idx_temp = head_idx

        for i in range(len(dics[importance])):
            if head_idx < dics[importance][i]:
                if i != 0:
                    head_idx = dics[importance][i-1]
                else:
                    break
                break

        if head_idx_temp == head_idx: # head_idx is in front of all doc_idx
            head_idx = dics[importance][-1]            

        count += len(dics[importance])

    # loop through dics[importance]
    start_idx = 0 # dics[target_importance] 's index
    for dics_idx in range(len(dics[target_importance])):
        if head_idx <= dics[target_importance][dics_idx]:
            start_idx = dics_idx
            break
    
    found = 0
    # print(f"start_idx: {start_idx}")
    idx = start_idx
    while idx < len(dics[target_importance]):
        count += 1
        if dics[target_importance][idx] == m:
            found = 1
            break
        idx += 1
    if found == 0:
        idx = 0
        while idx < len(dics[target_importance]):
            count += 1
            if dics[target_importance][idx] == m:
                found = 1
                break
            idx += 1

    print(count)
