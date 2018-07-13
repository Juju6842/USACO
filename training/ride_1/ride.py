"""
ID: justin62 
LANG: PYTHON3
TASK: ride
"""
fin = open('ride.in', 'r')
fout = open('ride.out', 'w')
comet = list(map(str, fin.readline().strip('\n')))
group = list(map(str, fin.readline().strip('\n')))
cometprod = 1
groupprod = 1
magic = 64
factor = 47
for x in comet:
    cometprod*=(ord(x)-magic)
for x in group:
    groupprod*=(ord(x)-magic)
if cometprod%factor == groupprod%factor:
    print('GO', file=fout)
else:
    print('STAY', file=fout)
fin.close()
fout.close()
