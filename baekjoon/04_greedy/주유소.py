# 13305

import sys

N = int(input())
road_cost = list(map(int, sys.stdin.readline().split()))
city_cost = list(map(int, sys.stdin.readline().split()))

road_cost.reverse()
city_cost.reverse()

total_cost = 0
c_min = city_cost.pop()
road_temp = 0
while road_cost:
    c = city_cost.pop()
    r = road_cost.pop()
    road_temp += r
    if c_min >= c:
        total_cost += road_temp*c_min
        c_min = c
        road_temp = 0
    else: # c_min < c
        continue
if road_temp:
    total_cost += road_temp*c_min
print(total_cost)

