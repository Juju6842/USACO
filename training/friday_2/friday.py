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
def thedayseachyear(theday, thisyear):
    for x in range (0, 12):
        caculated = theday%7
        for y in range (0,7):
            if caculated == y:
                tdem.append(y)
            else:
                y+=1
        '''0 is jan, 1 is feb, 2 is mar, etc.''' 
        '''Only caculates first year due to the task'''
        if x == 1 and thisyear%400 == 0:
            theday += 29 #if the year is an interval of 400
        elif x == 1 and thisyear%4 == 0 and thisyear%100 != 0:
            theday += 29 #if the year is an interval of 4 but not 100
        #the rest of the years plus the remaining calculations
        elif x == 3 or x == 5 or x == 8 or x == 10:
            theday += 30
        elif x == 1:    #this is feburary
            theday += 28
        else: #remaining months
            theday += 31
    return tdem
for x in range (0, int(yearamount[0])):
    thisyear = 1900 + x
    tdem = thedayseachyear(theday, thisyear)
    if thisyear % 400 == 0: 
        theday += 2
    elif thisyear%4 == 0 and thisyear%100 != 0:
        theday += 2
    else:
        theday += 1
result = [0, 0, 0, 0, 0, 0, 0]
for x in range (0, len(tdem)):
    result[tdem[x]] += 1
#giving all answers starting from saturday
outputseq = [6, 0, 1, 2, 3, 4, 5]
changeres = result[-1]
del result[-1]
result.insert(0, changeres)
strresult = []
for i in range(len(result)):
    strresult.append(str(result[i]))
print(' '.join(strresult), file=fout)
fin.close()
fout.close()
