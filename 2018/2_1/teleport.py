fin = open ('teleport.in', 'r')
fout = open ('teleport.out', 'w')
a = list(map(int, fin.readline().split()))
nomove = abs(a[1]-a[0])
yesmove = abs(a[0]-a[2]) + abs(a[1]-a[3])
othermove = abs(a[0]-a[3]) + abs(a[1]-a[2])
if nomove < yesmove and nomove < othermove:
    print(str(nomove), file=fout)
if yesmove < nomove and yesmove < othermove:
    print(str(yesmove), file=fout)
if othermove < nomove and othermove < yesmove:
    print(str(othermove), file=fout)
fin.close()
fout.close()
