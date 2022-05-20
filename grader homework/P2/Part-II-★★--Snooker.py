score = {'R':1, 'Y':2,'G':3,'W':4,'B':5,'P':6,'K':7}
p1,p2 = 0,0
r = 6
while r > 0:
    x = input()
    if x[1] == 'X':
        continue
    if x[1] == 'R':
        r -= 1
    if x[0] == '1':
        if x[1] == 'R' and x[2] != 'X':
            p1 += score[x[1]]+score[x[2]]
        elif x[1] == 'R' and x[2] == 'X':
            p1 += score[x[1]]
    elif x[0] == '2':
        if x[1] == 'R' and x[2] != 'X':
            p2 += score[x[1]]+score[x[2]]
        elif x[1] == 'R' and x[2] == 'X':
            p2 += score[x[1]]
r2 = 6
while r2 > 0:
    x = input()
    if x[1] != 'X':
        r2 -= 1
    else:
        continue
    if x[0] == '1':
        p1 += score[x[1]]
    elif x[0] == '2':
        p2 += score[x[1]]
print(p1,p2)
if p1 == p2: print('Tie')
elif p1 > p2: print('Player 1 wins')
elif p1 < p2: print('Player 2 wins')