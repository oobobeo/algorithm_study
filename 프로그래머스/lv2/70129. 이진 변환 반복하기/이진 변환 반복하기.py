def solution(s):
    answer = []
    def reduce(s):
        zeros = 0
        count = 0
        for i in s:
            if i == '1':
                count += 1
            else:
                zeros += 1
        return str(bin(count))[2:], zeros
    
    num = 0
    z_sum = 0
    while int(s) > 1:
        num += 1
        s,z = reduce(s)
        z_sum += z
    return [num, z_sum]
