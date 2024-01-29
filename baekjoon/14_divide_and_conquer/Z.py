# 1074

N,r,c = map(int, input().split())

order = 0
while True:
    order += 1
    if max(r,c) < 2**order:
        break

ans = 0
while order >= 1:
    division = 0
    if c >= 2**(order-1):
        division += 1
        c -= 2**(order-1)
    if r >= 2**(order-1):
        division += 2
        r -= 2**(order-1)
    ans += division*(2**(2*(order-1)))
    
    order -= 1
    

print(ans)
