fin = open ('mowing.in', 'r')
fout = open ('mowing.out', 'w')
a = int(fin.readline())
b = []
c = []
d = []
e = {}
time = 0
result = []
xcords = 0
ycords = 0
for x in range (a):
    b.append(list(map(str, fin.readline().split())))
for x in range (a):
    if b[x][0] == "N":
        for y in range (int(b[x][1])):
            xcords += 1
            c.append([xcords, ycords])
    elif b[x][0] == "S":
        for y in range (int(b[x][1])):
            xcords -= 1
            c.append([xcords, ycords])
    elif b[x][0] == "E":
        for y in range (int(b[x][1])):
            ycords += 1
            c.append([xcords, ycords])
    else:
        for y in range (int(b[x][1])):
            ycords -= 1
            c.append([xcords, ycords])
for z in range (len(c)):
    d.append(c.index(c[z]))
for z in range(len(d)):
    if d[z] != z:
        if d[z] in e:
            result.append(z - e[d[z]])
        else:
            result.append(z - d[z])
        e[d[z]] = z

if result == []:
    print (-1, file=fout)
else:
    print (str(min(result)), file=fout)
fin.close()
fout.close()
