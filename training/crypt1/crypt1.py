'''
ID: justin62
LANG: PYTHON3
TASK: crypt1
'''
fin = open('crypt1.in', 'r')
fout = open('crypt1.out', 'w')
digit = int(fin.readline().strip())
numbers = list(map(int,fin.readline().rstrip().rsplit()))
print (numbers)
result = 0
for x in numbers:
    for y in numbers:
        for z in numbers:
            for a in numbers:
                for b in numbers:
                    possible = [x*100+y*10+z, a, b]
                    possible.append(possible[0]*possible[1])
                    possible.append(possible[0]*possible[2])
                    possible.append(possible[0]*(possible[1]*10+possible[2]))
                    print (possible)
                    possible[3] = str(possible[3])
                    possible[4] = str(possible[4])
                    possible[5] = str(possible[5])
                    test = possible[3]+possible[4]+possible[5]
                    for c in range(len(test)):
                        if int(test[c]) in numbers:
                            if c == len(test)-1:
                                result += 1
                            continue
                        break
print (result)

fin.close()
fout.close()
