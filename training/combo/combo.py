'''
ID: justin62
LANG: PYTHON3
TASK: combo
'''
fin = open('combo.in', 'r')
fout = open('combo.out', 'w')
Comnum = int(fin.readline().rstrip())
comUno = list(map(int, fin.readline().rstrip().rsplit()))
comDos = list(map(int, fin.readline().rstrip().rsplit()))
result = 250
counted = []
overlap = 0
if Comnum < 6:
    result = Comnum**3
    print ((result), file=fout)
else:
    for x in range(0, 3):
        if (comUno[x]+Comnum) - 4 <= comDos[x]:
            comUno[x] += Comnum
            if abs(comUno[x]-comDos[x]) > 4:
                counted.append(0)
            else:
                counted.append(5-abs(comUno[x]-comDos[x]))
        elif (comDos[x]+Comnum) - 4 <= comUno[x]:
            comDos[x] += Comnum
            if abs(comDos[x]-comUno[x]) > 4:
                counted.append(0)
            else:
                counted.append(5-abs(comUno[x]-comDos[x]))
        elif abs(comUno[x]-comDos[x]) > 4:
            counted.append(0)
        else:
            counted.append(5-abs(comUno[x]-comDos[x]))
    overlap = counted[0]*counted[1]*counted[2]
    result -= overlap
    print ((result), file=fout)
fin.close()
fout.close()
