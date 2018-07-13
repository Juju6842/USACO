fin = open ('hoofball.in', 'r')
fout = open ('hoofball.out', 'w')
a = list(map(int, fin.readline().split()))
b = list(map(int, fin.readline().split()))
b.sort()
c = []
d = []
stuck = []
e = 0
m = a[0]-1
p = 1
p2 = 0
w = 1
f = 0
total_balls = 0
y = 1
z = 0
v = 0
d.append ([0, 1])
for x in range(m):
    c.append(b[p]-b[p2])
    p += 1
    p2 += 1
while z == 0:
    if w == m:
        d.append([w, 0])
        z += 1
    elif c[w] < c[f] and w < m:
        d.append([y, 1])
        y += 1
        w += 1
        f += 1
    elif c[f] <= c[w] and w < m:
        d.append([y, 0])
        y += 1
        w += 1
        f += 1
z -= 1
w -= w
f -= (f-1)
while z == 0:
    if w == m:
        z += 1
    elif d[w][1] == 1 and d[f][1] == 0:
        stuck.append([w,f])
        w += 1
        f += 1
    else:
        w += 1
        f += 1
z -= 1
w -= w
f -= (f-1)
ball = 0
while z == 0:
    leftNeighbor = stuck[ball][0]-1
    rightNeighbor = stuck[ball][1]+1
    origin = stuck[ball][0]
    origin2 = stuck[ball][1]
    if leftNeighbor >= 0:
        if d[leftNeighbor][1] == d[origin][1]:
            total_balls += 1
    if rightNeighbor <= m:
        if d[rightNeighbor][1] == d[origin2][1]:
            total_balls += 1
    if leftNeighbor >= 0 and rightNeighbor <= m:
        if d[leftNeighbor][1] != d[origin][1] and d[rightNeighbor][1] != d[origin2][1]:
            total_balls += 1
    if rightNeighbor > m and d[leftNeighbor][1] != d[origin][1]:
        total_balls += 1
    if leftNeighbor < 0 and d[rightNeighbor][1] != d[origin2][1]:
        total_balls += 1
    if leftNeighbor < 0 and rightNeighbor > m:
        total_balls += 1
    if ball == len(stuck)-1:
        z += 1
    else:
        ball += 1
print (str(total_balls), file=fout)
fin.close()
fout.close()

