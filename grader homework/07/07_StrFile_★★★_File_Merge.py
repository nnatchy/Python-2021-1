a = input().split()
k = []
for i in range(len(a)):
    fn = open(a[i],'r')
    test = []
    for line in fn:
        test.append(line)
    for j in range(0,len(test)-1):
        test[j] = test[j][:-1]
        k.append(test[j])
    k.append(test[-1])
bro = []
for i in range(len(k)):
    x = k[i].split(' ')
    bro.append(x)
for i in range(len(bro)):
    bro[i].insert(0,bro[i][0][-2:])
bro = sorted(bro)
for i in range(len(bro)):
    bro[i].pop(0)
for i in range(len(bro)):
    print(bro[i][0] +' '+ bro[i][1])






