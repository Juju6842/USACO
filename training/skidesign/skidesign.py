'''
ID: justin62
LANG: PYTHON3
TASK: skidesign
'''
def completeExam(hillhights, hillamt, totalprice):
    needchange = hillhights[hillamt-1-x]-hillhights[x]
    needchange -= 17
    if needchange > 0:
        onecheck = needchange%2
        needchange -= onecheck
        totalprice += (needchange/2)**2
        totalprice += (needchange/2+onecheck)**2
    return totalprice
fin = open('skidesign.in', 'r')
fout = open('skidesign.out', 'w')
hillamt = int(fin.readline().rstrip())
hillhights = []
totalprice = 0
for x in range(hillamt):
    hillhights.append(int(fin.readline().strip()))
hillhights.sort()
for x in range(hillamt):
    totalprice = completeExam(hillhights, hillamt, totalprice)
print ((int(totalprice)), file=fout)
fin.close()
fout.close()
