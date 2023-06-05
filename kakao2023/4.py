def solution(numbers):
    
    from itertools import product
    import bisect
    
    # 2^5(layer 5) 까지 뽑아 놓기 (len=390625)
    # 2^6(layer 6)는 따로 계산
    
    possible = [2,3,6,7]
    total = possible[:] + [1]
    for i in range(3):
        temp = []
        possible += [0]
        for comb in product(possible, repeat=2):
            temp.append( (comb[0]<<( 2**(i+2) )) + 2**(2**(i+2)-1) + comb[1])
        possible = temp[:]
        total += possible
        # break
    # print(possible)
    # print(len(total))
    total.sort()
    # print(list(map(bin, total[-10:])))
    # print(list(map(bin, total[:10])))
    
    answer = []
    for number in numbers:
        if number <= 2**31 -1:
            l = bisect.bisect_left(total, number)
            if l <= len(total)-1 and total[l] == number:
                answer.append(1)
            else:
                answer.append(0)
        else:
            left = number >> 32
            right = (number - (left<<32)) - (2**31)
            l, r = bisect.bisect_left(total, left), bisect.bisect_left(total, right)
            # print(number, left, right)
            # print(l,r, len(total), total[-1])
            # print('---------------')
            # print(l, total[l], r, total[r])
            if l<= len(total)-1 and left == total[l] and right == total[r]:
                answer.append(1)
            else:
                answer.append(0)
            
    return answer

print(solution([42,63,111,95, 2**63-1, 2147483647]))
