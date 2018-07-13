"""
ID: justin62
LANG: PYTHON3
TASK: gift1
"""
fin = open('gift1.in', 'r')
fout = open('gift1.out','w')
friendmoney = {}
amt = int(fin.readline().strip('\n'))
people = []
answer = []
for x in range(0, int(amt)):
    people.append(fin.readline().strip('\n'))
for x in range(0, int(amt)):
    friendmoney[people[x]] = 0
for x in range(0, int(amt)):
    transaction = []
    transaction.append(fin.readline().strip('\n'))
    transaction.append(fin.readline().strip('\n').split())
    for y in range(0, int(transaction[1][1])):
        transaction.append(fin.readline().strip('\n'))
    if int(transaction[1][1]) != 0:
        returnvalue = int(int(transaction[1][0])%int(transaction[1][1]))
        givevalue = int((int(transaction[1][0])-returnvalue)/int(transaction[1][1]))
        friendmoney[transaction[0]] -= (int(transaction[1][0])-returnvalue)
    elif transaction[1][1] == 0:
        returnvalue = int(transaction[1][0])
        friendmoney[transaction[0]]+=returnvalue
    for z in range(0, int(transaction[1][1])):
        friendmoney[transaction[z+2]] += givevalue
for x in range(0, int(amt)):
    print (people[x]+' '+str(friendmoney[people[x]]), file=fout)
fin.close()
fout.close()
