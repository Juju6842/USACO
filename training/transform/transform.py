'''
ID: justin62
LANG: PYTHON3
TASK: transform
'''
def rotation(figure):
    possible = [['-' for x in range(length)] for y in range (length)]
    for x in range (length):
        for y in range (length):
            if figure[x][y] == '@':
                possible[y][length-1-x] = figure[x][y]
    return possible
def reflection (figure):
    possible = [['-' for x in range(length)] for y in range (length)]
    for x in range (length):
        for y in range (length):
            if figure[x][y] == '@':
                possible[x][length-1-y] = figure[x][y]
    return possible
fin = open('transform.in', 'r')
fout = open('transform.out', 'w')
length = int(fin.readline())
if length == 1:
    print (('1'), file=fout)
figure = []
result = []
var = 0
for x in range (length):
    figure.append(list(fin.readline().strip()))
for x in range (length):
    result.append(list(fin.readline().strip()))
firstanswer = rotation(figure)
secondanswer = rotation(firstanswer)
thirdanswer = rotation(secondanswer)
fourthanswer = reflection(figure)
fifthanswera = rotation(fourthanswer)
fifthanswerb = rotation(fifthanswera)
fifthanswerc = rotation(fifthanswerb)
if firstanswer == result:
    print (('1'), file=fout)
elif secondanswer == result:
    print (('2'), file=fout)
elif thirdanswer == result:
    print (('3'), file=fout)
elif fourthanswer == result:
    print (('4'), file=fout)
elif fifthanswera == result or fifthanswerb == result or fifthanswerc == result:
    print (('5'), file=fout)
elif figure == result:
    print (('6'), file=fout)
else:
    print (('7'), file=fout)
fin.close
fout.close
