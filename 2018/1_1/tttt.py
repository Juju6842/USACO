fin = open ('tttt.in', 'r')
fout = open ('tttt.out', 'w')
a = list(map(str, fin.readline()))
b = list(map(str, fin.readline()))
c = list(map(str, fin.readline()))
a = a[:-1]
b = b[:-1]
c = c[:-1]
d = []
solowin = set()
for x in range (0, 3):
    if a[0] == a[1] == a[2]:
        solowin.add(a[0])
    if b[0] == b[1] == b[2]:
        solowin.add(b[0])
    if c[0] == c[1] == c[2]:
        solowin.add(c[0])
    if a[0] == b[1] == c[2]:
        solowin.add(a[0])
    if a[2] == b[1] == c[2]:
        solowin.add(a[2])
    if a[x] == b[x] == c[x]:
        solowin.add(a[x])
if a[0] == a[1] or a[0] == a[2] or a[1] == a[2]:
    if a[0] != a[1] or a[0] != a[2] or a[1] != a[2]:
        d.append([a[0],a[1],a[2]])
if b[0] == b[1] or b[0] == b[2] or b[1] == b[2]:
    if b[0] != b[1] or b[0] != b[2] or b[1] != b[2]:
        d.append([b[0],b[1],b[2]])
if c[0] == c[1] or c[0] == c[2] or c[1] == c[2]:
    if c[0] != c[1] or c[0] != c[2] or c[1] != c[2]:
        d.append([c[0],c[1],c[2]])
if a[0] == b[0] or a[0] == c[0] or b[0] == c[0]:
    if a[0] != b[0] or a[0] != c[0] or b[0] != c[0]:
        d.append([a[0],b[0],c[0]])
if a[1] == b[1] or a[1] == c[1] or b[1] == c[1]:
    if a[1] != b[1] or a[1] != c[1] or b[1] != c[1]:
        d.append([a[1],b[1],c[2]])
if a[2] == b[2] or a[2] == c[2] or b[2] == c[2]:
    if a[2] != b[2] or a[2] != c[2] or b[2] != c[2]:
        d.append([a[2],b[2],c[2]])
if a[0] == b[1] or a[0] == c[2] or b[1] == c[2]:
    if a[0] != b[1] or a[0] != c[2] or b[1] != c[2]:
        d.append([a[0],b[1],c[2]])
if a[2] == b[1] or a[2] == c[0] or b[1] == c[0]:
    if a[2] != b[1] or a[2] != c[0] or b[1] != c[0]:
        d.append([a[2],b[1],c[0]])
teamwins = []
for x in range(len(d)):
    if set(d[x]) not in teamwins:
        teamwins.append(set(d[x]))

print(str(len(solowin)), file=fout)
print(str(len(teamwins)), file=fout)
fin.close()
fout.close()

