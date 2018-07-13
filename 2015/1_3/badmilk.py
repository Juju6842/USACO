fin = open ('badmilk.in', 'r')
fout = open ('badmilk.out', 'w')
z = 0
a = list(map(int, fin.readline().split()))
b = list(map(int, fin.readline().split()))
c = list(map(int, fin.readline().split()))
d = list(map(int, fin.readline().split()))
e = list(map(int, fin.readline().split()))
f = list(map(int, fin.readline().split()))
g = list(map(int, fin.readline().split()))
h = list(map(int, fin.readline().split()))
i = list(map(int, fin.readline().split()))
j = list(map(int, fin.readline().split()))
tel = []
for i in range (0, a[2]):
    tel.append (i)
print (tel)
print(str(z), file=fout)
fin.close
fout.close
