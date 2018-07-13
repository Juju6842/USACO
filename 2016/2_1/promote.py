fin = open ('promote.in', 'r')
fout = open ('promote.out', 'w')
a = list(map(int, fin.readline().split()))
b = list(map(int, fin.readline().split()))
c = list(map(int, fin.readline().split()))
d = list(map(int, fin.readline().split()))
p = d[1]-d[0]
if p > 0:
    c[0] = c[0] - p
    g = c[1] - c[0]
else:
    g = c[1] - c[0]
if g > 0:
    b[0] = b[0] - g
    s = b[1] - b[0]
else:
    s = b[1] - b[0]

print(str(s), file=fout)
print(str(g), file=fout)
print(str(p), file=fout)
fin.close()
fout.close()
