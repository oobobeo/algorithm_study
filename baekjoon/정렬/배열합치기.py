# 11728









N, M = map(int, input().split())
list1 = list( map(int, input().split()) )
list2 = list( map(int, input().split()) )

list1_len = len(list1)
list2_len = len(list2)
result = [0]*(list1_len + list2_len)
i = 0
j = 0
while True:
    if i >= list1_len:
        for k in range(j, list2_len):
            result[i+k] = list2[k]
        break
    if j >= list2_len:
        for k in range(i, list1_len):
            result[j+k] = list1[k]
        break

    if list1[i] <= list2[j]:
        result[i+j] = list1[i]
        i += 1
    else:
        result[i+j] = list2[j]
        j += 1

print(' '.join(map(str, result)))