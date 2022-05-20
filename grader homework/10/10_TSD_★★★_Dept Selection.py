d = {}
for i in range(int(input())):
    total = input().split()
    d[total[0]] = int(total[1])
l = []
for i in range(int(input())):
    stu = input().split()
    l.append([float(stu[1]),stu[0],stu[2:]])
l.sort()
l1 = []
for score,id,paak in l[::-1]:
    for i in paak:
        if d[i] > 0:
            d[i] = d[i] - 1
            l1.append([id,i])
            break
l1.sort()
for i in l1:
    print(i[0],i[1])