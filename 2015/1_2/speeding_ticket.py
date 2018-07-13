fin = open ('speeding.in', 'r')
fout = open ('speeding.out', 'w')
road,act = map(int, fin.readline().split())
road_limit = []
act_limit = []
result = []
for x in range (road):
    road_limit.append(list(map(int, fin.readline().split())))

for x in range (act):
    act_limit.append(list(map(int, fin.readline().split())))

rlIndex = 0
alIndex = 0
while True:
    speed_dif = act_limit[alIndex][1] - road_limit[rlIndex][1]
    dis_dif = act_limit[alIndex][0] - road_limit[rlIndex][0]
    result.append(speed_dif)
    if dis_dif > 0:
        act_limit[alIndex][0] -= road_limit[rlIndex][0]
        rlIndex += 1
    elif dis_dif < 0:
        road_limit[rlIndex][0] -= act_limit[alIndex][0]
        alIndex += 1
    else:
        rlIndex += 1
        alIndex += 1
    if rlIndex == len(road_limit) and alIndex == len(act_limit):
        break
if max(result) < 0:
    fout.write(str(0))
else:
    fout.write(str(max(result)))
fin.close()
fout.close()

