'''
ID: justin62
LANG: PYTHON3
TASK: beads
'''
def shrink(necklace, size, number):
    bcount = 0
    rcount = 0
    wcount = 0
    for x in range(len(necklace)):
        if necklace[x] == 'w':
            if bcount != 0:
                size.append('b')
                number.append(bcount)
                bcount = 0
            if rcount != 0:
                size.append('r')
                number.append(rcount)
                rcount = 0
            wcount += 1
        elif necklace[x] == 'b':
            if wcount != 0:
                size.append('w')
                number.append(wcount)
                wcount = 0
            if rcount != 0:
                size.append('r')
                number.append(rcount)
                rcount = 0
            bcount += 1
        elif necklace[x] == 'r':
            if wcount != 0:
                size.append('w')
                number.append(wcount)
                wcount = 0
            if bcount != 0:
                size.append('b')
                number.append(bcount)
                bcount = 0
            rcount += 1
        if x == len(necklace)-1:
            if wcount != 0:
                size.append('w')
                number.append(wcount)
            elif rcount != 0:
                size.append('r')
                number.append(rcount)
            elif bcount != 0:
                size.append('b')
                number.append(bcount)
    return size
def extend(size, number):
    for x in range (len(size)):
        size.append(size[x])
        number.append(number[x])
def combine(size):
    for x in range(len(size)):
        if len(size) == 1:
            break
        elif x == len(size)-1:
            break
        elif size[x] == 'w':
            if size[x-1] == size[x+1] == 'b':
                size[x] = 'b'
            if size[x-1] == size[x+1] == 'r':
                size[x] = 'r'
def returntoplace(size):
    necklace = []
    for x in range(len(size)):
        for y in range(int(number[x])):
            necklace.append(size[x])
    return necklace
def thedivide(size, number):
    x = 0
    while True:
        if x == len(size) - 1:
            break
        elif size[x] != 'w' and size[x+1] != 'w':
            size.insert(x+1, 'w')
            number.insert(x+1, '0')
        x += 1
    return size
'''def whitedecision(size):
    for x in range(len(size)):
        if size[x] == 'w' and int(number[x]) > 0:
            if (int(number[x-1]) + int(number[x-3])) > (int(number[x+1]) + int(number[x+3])):
                size[x] = size[x-1]
            if (int(number[x-1]) + int(number[x-3])) < (int(number[x+1]) + int(number[x+3])):
                size[x] = size[x+1]
    return size'''
def thefinish(size):
    num = 0
    for x in range(0, len(size)):
        num1 = 0
        if x == len(size)-5:
            break
        else:
            if size[x] == 'w':
                num1 = int(number[x]) + int(number[x+1]) + int(number[x+2]) + int(number[x+3]) + int(number[x+4])
                if num1 > num:
                    num = num1
            if size[x] == 'b' or size[x] == 'r':
                num1 = int(number[x]) + int(number[x+1]) + int(number[x+2]) + int(number[x+3])
                if num1 > num:
                    num = num1

    return num
fin = open('beads.in', 'r')
fout = open('beads.out', 'w')
amount = fin.readline().rstrip()
necklace = list(fin.readline().rstrip())
size = []
number = []
size = shrink(necklace, size, number)
if len(size) == 1:
    print(str(number[0]), file=fout)
elif len(size) == 2:
    print(str(int(number[0]+number[1])), file=fout)
elif len(size) == 3:
    for x in range(len(size)):
        if size[x][0] == 'w':
            print(str(int(number[0]+number[1]+number[2])), file=fout)
elif not 'r' in size or not 'b' in size:
    y = 0
    for x in range(len(size)):
        y += int(number[x])
    print ((y), file=fout)
else:
    extend(size, number)
    combine(size)
    necklace = returntoplace(size)
    size = []
    number = []
    size = shrink(necklace, size, number)
    thedivide(size, number)
    '''size = whitedecision(size)'''
    num = thefinish(size)
    if len(size) > 3:
        print(str(num), file=fout)
fin.close()
fout.close()
