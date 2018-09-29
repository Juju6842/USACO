'''
ID: justin62
LANG: PYTHON3
TASK: milk2
'''
def consec(times, contest, higher, x):
    stop = times[x][1]
    for i in range(x, int(farmAmt)):
        if len(times)-1 == i:
            contest = times[i][1]
            break
        elif stop >= times[i+1][0]:
            if times[i+1][1] > stop:
                stop = times[i+1][1]
            continue
        elif stop < times[i+1][0]:
            contest = stop
            higher = contest
            break
    return contest, higher
def overlap(times, contest, higher, x):
    for a in range(x+1, int(farmAmt)):
        if len(times)-1 == a:
            contest = times[x][1]
            higher = times[x][1]
            break
        elif times[a][1] <= times[x][1]:
            continue
        elif times[a][1] > times[x][1] and times[a][0] <= times[x][1]:
            x = a
            contest, higher = consec(times, contest, higher, x)
    return contest, higher
fin = open('milk2.in', 'r')
fout = open('milk2.out', 'w')
farmAmt = fin.readline()
times = []
start = 0
idle = 0
contest = 0
higher = 0
for x in range (0, int(farmAmt)):
    times.append(list(map(int, fin.readline().split())))
times.sort()
if int(farmAmt) == 1:
    start = times[0][1]-times[0][0]
for x in range (0, int(farmAmt)):
    if len(times)-1 == x:
        break
    if times[x][1] < higher:
        continue
    if times[x][0] <= times[x+1][0] and times[x][1] >= times[x+1][1]:
        contest, higher = overlap(times, contest, higher, x)
        contest -= times[x][0]
        if contest > start:
            start = contest
    elif times[x][1] < times[x+1][0]:
        contest = times[x+1][0] - times[x][1]
        if contest > idle:
            idle = contest
    elif times[x][1] >= times[x+1][0]:
        contest, higher = consec(times, contest, higher, x)
        contest -= times[x][0]
        if contest > start:
            start = contest
if start == 0:
    for x in range(0, int(farmAmt)-1):
        contest = times[x][1] - times[x][0]
        if contest > start:
            start = contest
strres = []
strres.append(str(start))
strres.append(str(idle))
print (' '.join(strres), file=fout)
fin.close()
fout.close()
