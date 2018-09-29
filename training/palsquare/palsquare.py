'''
ID: justin62
LANG: PYTHON3
TASK: palsquare
'''
def convert(x, base):
    y = True
    num = []
    while y == True:
        if x == 0:
            y = False
        else:
            placenum = (x%base)
            inputnum.append(placenum)
            x -= x % base
            x = x//base
    return inputnum
fin = open('palsquare.in', 'r')
fout = open('palsquare.out', 'w')
base = int(fin.readline())
result = []
conversion = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9',  10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15: "F", 16: "G", 17: "H", 18: "I", 19: "J"}
for x in range (1, 301):
    inputnum = []
    palidromes = []
    inputnum = convert(x, base)
    for z in range (len(inputnum)):
        palidromes.append(conversion[inputnum[z]])
    palidromes = palidromes[::-1]
    notsquare = ''.join(palidromes)
    inputnum = []
    palidromes = []
    x = x**2
    inputnum = convert(x, base)
    for z in range (len(inputnum)):
        palidromes.append(conversion[inputnum[z]])
    palidromes = palidromes[::-1]
    possible = ''.join(palidromes)
    if possible==possible[::-1]:
        result.append([notsquare, possible])
for x in range(len(result)):
    complete = []
    complete.append(str(result[x][0]))
    complete.append(str(result[x][1]))
    print (' '.join(complete), file=fout)
fin.close()
fout.close()
