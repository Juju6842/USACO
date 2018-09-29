'''
ID: justin62
LANG: PYTHON3
TASK: namenum
'''
def meaningfulName(number):
    if len(number) == 1:
        return list(referal[number])
    else:
        firstnum = list(referal[number[0]])
        lastnum = meaningfulName(number[1:])
        returnlist = []
        for c in firstnum:
            for x in lastnum:
                returnlist.append(c+x)
        return returnlist
fin = open('namenum.in', 'r')
fout = open('namenum.out', 'w')
dictionary = open('dict.txt', 'r')
names = set(i.rstrip() for i in dictionary)
number = fin.readline().rstrip()
referal= {
        '2': "ABC",
        '3': "DEF",
        '4': "GHI",
        '5': "JKL",
        '6': "MNO",
        '7': "PRS",
        '8': "TUV",
        '9': "WXY"
        }
possibleNames = meaningfulName(number)
possibleresults = set(possibleNames) & names
endresults = sorted(list(possibleresults))
if endresults == []:
    print (('NONE'), file=fout)
else:
    for x in range(len(endresults)):
        print ((endresults[x]), file=fout)
fin.close()
fout.close()

