ids = []
grades = []
total = []
while True:
    a = input()
    if a == 'q':
        break
    d = a.split()
    total = total + d
for i in range(len(total)):
    if i%2 == 0:
        ids.append(total[i])
    else:
        grades.append(total[i])
check = input().split()
list1 = ['A','B+','B','C+','C','D+','D','F']
for i in range(len(check)):
    if check[i] in ids:
        k = ids.index(check[i])
        if grades[k] != 'A':
            grades[k] = list1[list1.index(grades[k])-1]
        else:
            grades[k] = list1[list1.index(grades[k])]
ruam = []
for i in range(len(ids)):
    ruam = ruam + [[ids[i],grades[i]]]
ruam.sort()
for i in range(len(ruam)):
    print(ruam[i][0],ruam[i][1])