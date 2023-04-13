# 22864







A,B,C,M = map(int, input().split())





total_work = 0
total_stress = 0
for _ in range(24):
    if total_stress + A <= M:
        total_work += B
        total_stress += A
    else:
        total_stress -= C
        total_stress = max(0, total_stress)
        
print(total_work)
