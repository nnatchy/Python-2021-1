inp = input().split()
deli = []
while inp != ['END']:
    deli.append([inp[0], inp[1], int(inp[2]), int(inp[3]), int(inp[4])])
    inp = input().split()
role = ['E', 'Q', 'N', 'F']
ndate = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
undate = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
deli_error,date_error,month_error,year_error,correct = [],[],[],[],[]
for i in range(len(deli)):
    year = deli[i][4] - 543
    if deli[i][4] < 2558:
        year_error.append(deli[i])  # ok
        print('Error: %s %s %s %s %s --> Invalid year' %(year_error[0][0],year_error[0][1],year_error[0][2],year_error[0][3],year_error[0][4]))
        year_error.pop(0)

    elif deli[i][3] < 1 or deli[i][3] > 12:
        month_error.append(deli[i])  # ok
        print('Error: %s %s %s %s %s --> Invalid month' %(month_error[0][0],month_error[0][1],month_error[0][2],month_error[0][3],month_error[0][4]))
        month_error.pop(0)
            
    elif (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):  # leap okay
        if deli[i][2] > undate[deli[i][3]] or deli[i][2] < 1:
            date_error.append(deli[i])
            print('Error: %s %s %s %s %s --> Invalid date' %(date_error[0][0],date_error[0][1],date_error[0][2],date_error[0][3],date_error[0][4]))
            date_error.pop(0)
        elif (deli[i][1] not in role) or (deli[i][1] == 'X'):
            deli_error.append(deli[i])  # ok
            print('Error: %s %s %s %s %s --> Invalid delivery type' %(deli_error[0][0],deli_error[0][1],deli_error[0][2],deli_error[0][3],deli_error[0][4]))
            deli_error.pop(0)
        elif deli[i][2] <= undate[deli[i][3]] or deli[i][2] >= 1:
            correct.append([deli[i][4], deli[i][3], deli[i][2], deli[i][0], deli[i][1]])       

    elif deli[i][2] > ndate[deli[i][3]] or deli[i][2] < 1:  # okay
        date_error.append(deli[i])
        print('Error: %s %s %s %s %s --> Invalid date' %(date_error[0][0],date_error[0][1],date_error[0][2],date_error[0][3],date_error[0][4]))
        date_error.pop(0)

    elif (deli[i][1] not in role) or (deli[i][1] == 'X'):
        deli_error.append(deli[i])  # ok
        print('Error: %s %s %s %s %s --> Invalid delivery type' %(deli_error[0][0],deli_error[0][1],deli_error[0][2],deli_error[0][3],deli_error[0][4]))
        deli_error.pop(0)
     
    else:
        correct.append([deli[i][4], deli[i][3], deli[i][2], deli[i][0], deli[i][1]])

correct = sorted(correct)

for i in range(len(correct)):
    if correct[i][4] == 'E':
        correct[i][2] += 1
    elif correct[i][4] == 'Q':
        correct[i][2] += 3
    elif correct[i][4] == 'N':
        correct[i][2] += 7
    elif correct[i][4] == 'F':
        correct[i][2] += 14

for i in range(len(correct)):
    year = correct[i][0] - 543
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        if correct[i][2] > undate[correct[i][1]]:
            correct[i][2] -= undate[correct[i][1]]
            if correct[i][1] == 12:
                correct[i][1] = 1
                correct[i][0] += 1
            else:
                correct[i][1] += 1   
    else:
        if correct[i][2] > ndate[correct[i][1]]:
            correct[i][2] -= ndate[correct[i][1]]
            if correct[i][1] == 12:
                correct[i][1] = 1
                correct[i][0] += 1
            else:
                correct[i][1] += 1
correct = sorted(correct)

def printcorrect(l):
    for i in l:
        if len(l) != 0:
            print('%s: delivered on %d/%d/%d' %((i[3]),i[2],i[1],i[0]))
printcorrect(sorted(correct))