'''
ID: justin62
LANG: PYTHON3
TASK: dualpal
'''
def convert(possible, x):
    y = True
    num = []
    while y == True:
        if possible == 0:
            y = False
        else:
            placenum = (possible%(x))
            inputnum.append(placenum)
            possible -= possible % (x)
            possible = possible//(x)
    return inputnum
fin = open('dualpal.in', 'r')
fout = open('dualpal.out', 'w')
amount, number = fin.readline().rstrip().rsplit()
conversion = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
result = [] 
check = []
possible = number
for x in range (1, int(amount)+1):
    palidromes = []
    if len(result) >= int(amount):
        break
    while True:
        possible = int(possible)+1
        for x in range (2, 11):
            inputnum = []
            inputnum = convert(possible, x)
            palidromes = []
            for z in range (len(inputnum)):
                palidromes.append(conversion[inputnum[z]])
            palidromes = palidromes[::-1]
            contest = ''.join(palidromes)
            if contest == contest[::-1]:
                check.append(contest)
        if len(check) >= 2:
            result.append(possible)
            check = []
            break
        else:
            check = []
            continue

for x in range(len(result)):
    print(str(result[x]), file=fout)
fin.close()
fout.close()
