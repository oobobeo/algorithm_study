# 11729


N = int(input())

# src, dst are one of [1,2,3]
# move n disks. src -> dst
count = 0
moves = []
def move(src, dst, n):
    global count
    # base cond
    if n == 1:
        count += 1
        moves.append(f"{src} {dst}")
        return
    move(src, 6-src-dst, n-1)
    moves.append(f"{src} {dst}")
    count += 1
    move(6-src-dst, dst, n-1)

move(1,3,N)
print(count)
for m in moves:
    print(m)

