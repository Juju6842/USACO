"""
ID: justin62
LANG: PYTHON3
TASK: friday
"""
from collections import deque
'''def completechange_start (theday, tdem, caculated, theactual start):
    '''
fin = open('friday.in', 'r')
fout = open('friday.out', 'w')
yearamount = []
yearamount.append(fin.readline().rstrip())
#tdem = the day each month
tdem = []
theday = 13
for x in range (0, 12):
    caculated = theday%7
    for y in range (0,7):
        if caculated == y:
            tdem.append(y)
        else:
            y+=1
    '''0 is jan, 1 is feb, 2 is mar, etc.''' 
    '''Only caculates first year due to the task'''
    if x == 3 or x == 5 or x == 8 or x == 10:
        theday = theday + 30
    elif x == 1:    #this is feburary
        theday = theday + 28
    else: #remaining months
        theday = theday + 31

result=[0, 0, 0, 0, 0, 0, 0]
for x in range (0, 12):
    result[tdem[x]] = result[tdem[x]] + 1
    adding = deque(result)
#leap year starts in march, so that means I got to work on that
for x in range (0, int(yearamount[0])-1):
    thisyear = 1900 + x+1
    print (thisyear)
    if thisyear%400 == 0:
        adding.rotate(2)
        for x in range (0,7):
            result[x] = result[x] + adding[x]
    elif thisyear%4 == 0 and thisyear%100 != 0:
        adding.rotate(2)
        theactualstart = (x+1)%7

        for x in range (0,7):
            result[x] = result[x] + adding[x]
    else:
        adding.rotate(1)
        for x in range (0,7):
            result[x] = result[x] + adding[x]
    print (adding[0])
    print (result[0])
#giving all answers starting from saturday
outputseq = [6, 0, 1, 2, 3, 4, 5]
for x in outputseq:
    print (str(result[x]) + ' ') 
fin.close()
fout.close()
