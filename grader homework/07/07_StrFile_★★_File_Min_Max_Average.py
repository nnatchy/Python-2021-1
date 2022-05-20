data = input().split()
fin = open(data[0])
l = []
for line in fin.readlines() :
    line = line.split()
    if line[0][:2] == data[1][-2:] : l.append(float(line[1]))
if len(l) == 0 : print('No data')
else : print(min(l),max(l),sum(l)/len(l))