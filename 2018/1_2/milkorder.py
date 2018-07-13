fin = open ('milkorder.in', 'r')
fout = open ('milkorder.out', 'w')
a = list(map(int, fin.readline().split()))
b = list(map(int, fin.readline().split()))
c = []
cowtoposdict = {}
postocowdict = {}
e = 1
f = 0
g = 1
def findemptyspotfromtail(postocowdict, insertIndex, cow):
    while insertIndex > 0 :
        if cow == 1:
            insertIndex = 1
            if postocowdict[insertIndex] == 0:
                return insertIndex
            else:
                insertIndex += 1
        if cow != 1:
            if postocowdict[insertIndex] == 0:
                return insertIndex
            else:
                insertIndex -= 1
    return 0

for x in range (a[0]):
    postocowdict[e] = 0
    e += 1
for x in range (a[2]):
    c.append(list(map(int, fin.readline().split())))
for x in range (a[2]):
    cowtoposdict[c[f][0]] = c[f][1]
    postocowdict[c[f][1]] = c[f][0]
    f += 1
if 1 in cowtoposdict:
    print (str(cowtoposdict[1]))
    print (str(cowtoposdict[1]), file=fout)

for x in range (len(b)):
    insertIndex = a[0]
    for index in range (len(b)-1, -1, -1):
        cow = b[index]
        if cow in cowtoposdict:
            insertIndex = cowtoposdict[cow]
        else:
            pos = findemptyspotfromtail(postocowdict, insertIndex, cow)
            cowtoposdict[cow] = pos
            postocowdict[pos] = cow
            if 1 in b:
                print(str(insertIndex), file=fout)
while True:
    if postocowdict[g] == 0:
        print(str(g), file=fout)
        break
    else:
        g += 1
fin.close()
fout.close()
