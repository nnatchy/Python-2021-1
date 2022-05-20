import numpy as np

n = int(input())
cond = int(input())
table = np.zeros((n,n),int)
for i in range(n):
    eRow = np.array([int(e) for e in input().split()])
    table[i,] = eRow
ind = np.arange(0,cond)
lu2rd = []
ld2ru = []
winner = []
playar = [0,1,2]
error = []
for row in table:
    for i in row:
        if i not in playar:
            error.append(1)
if len(error) != 0:
    print('ERROR')
else:
    sec = []
    for i in range(n-cond+1):
        for j in range(n-cond+1):
            se3c.append(np.array(table[i:i+cond, j:j+cond]))
    for t in sec:
        for i in range(2):
            count = 0
            row = []
            col = []
            for j in t[i]:
                row.append(j)
            for j in range(len(row)-n+1):
                check = row[j]
                cnt = 0
                for k in row[j:j+n]:
                    if k == check:
                        cnt += 1
                    if cnt == cond:
                        winner.append(check)
                        break
            
            for j in t[:,i]:
                col.append(j)
            for j in range(len(col)-n+1):
                check = col[j]
                cnt = 0
                for k in col[j:j+n]:
                    if k == check:
                        cnt += 1
                    if cnt == cond:
                        winner.append(check)
                        break
        for i in range(1):
            for l in t[ind,ind]:
                lu2rd.append(l)
            for l in range(len(lu2rd)-n+1):
                check = lu2rd[l]
                cnt = 0
                for k in lu2rd[l:l+n]:
                    if k == check:
                        cnt += 1
                    if cnt == cond:
                        winner.append(check)
                        break
        for i in range(1):
            for l in t[ind,ind[::-1]]:
                ld2ru.append(l)
            for l in range(len(ld2ru)-n+1):
                check = ld2ru[l]
                cnt = 0
                for k in ld2ru[l:l+n]:
                    if k == check:
                        cnt += 1
                    if cnt == cond:
                        winner.append(check)
                        break
    lastcheck = []
    if len(winner) == 0:
        print('DRAW')
    else:
        if 0 in winner:
            if (2 not in winner) and (1 not in winner):
                print('NOT OVER')
        if len(winner) >= 1:
            d = {k:1 for k in winner}
            if len(d) == 2:
                for key in d:
                    if key != 0:
                        lastcheck.append(key)
            else:
                for i in range(len(winner)):
                    if winner[i-1] != winner[i]:
                        print('ERROR')
                        break
                    else:
                        lastcheck.append(winner[i])
        for i in lastcheck:
            print(i,'WIN')
            break