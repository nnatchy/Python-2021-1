list1 = []
a = input()
while a != 'q':
    x = float(a)
    list1.append(x)
    a = input()
if len(list1) == 0:
    print('No Data')
total = 0
for i in range(len(list1)):
    total = total + list1[i]
if len(list1) > 0:
    print(round(total/len(list1),2))