'''
ID: justin62
LANG: PYTHON3
TASK: milk
'''
fin = open('milk.in', 'r')
fout = open('milk.out', 'w')
amountTotal, farmers = fin.readline().rstrip().rsplit()
amountTotal = int(amountTotal)
farmers = int(farmers)
cost = []
productamt = 0
finaltotal = 0
for x in range(farmers):
    cost.append(fin.readline().strip().split())
cost = [[int(float(j)) for j in i] for i in cost]
cost.sort()
for x in range(farmers):
    if amountTotal-cost[x][1] == 0:
        productamt = cost[x][1]
        finaltotal += (productamt*cost[x][0])
        break
    elif amountTotal-cost[x][1] < 0:
        productamt = amountTotal
        finaltotal += (productamt*cost[x][0])
        break
    elif amountTotal-cost[x][1] > 0:
        amountTotal -= cost[x][1]
        finaltotal += (cost[x][1]*cost[x][0])
print ((finaltotal), file=fout)
