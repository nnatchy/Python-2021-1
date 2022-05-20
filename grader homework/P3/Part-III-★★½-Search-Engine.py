data = []
for i in range(int(input())):
    nf = input()
    txt = input()
    data.append([nf, txt])
search = input()
lscore = []
while search != '-1':
    l5 = []
    for i in range(len(data)):
        count = 0
        temp = data[i][1].split(' ')
        for j in temp:
            if search == j:
                count += 1
        stemp = set(temp)
        l5.append([(count/len(temp))*(1/len(stemp)), data[i][0]])
    lscore.append(l5)
    search = input()
final = []
for i in lscore:
    i.sort()
    if i[-1][0] == 0.0:
        final.append('NOT FOUND')
    else:
        final.append(i[-1][1])
for i in final:
    print(i)
