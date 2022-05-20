a = input();b = input()
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
date1 = [];date2 = []
for i in a:
    if i == ',':
        pass
    else:
        date1.append(i)
for i in b:
    if i == ',':
        pass
    else:
        date2.append(i)
temp1 = '';temp2 = ''
for i in date1:
    temp1 = temp1 + i
for i in date2:
    temp2 = temp2 + i
list1 = temp1.split();list2 = temp2.split()
if int(list1[3]) > int(list2[3]):
    print(list2[0])
elif int(list1[3]) < int(list2[3]):
    print(list1[0])
else:
    if months.index(list1[1]) > months.index(list2[1]):
        print(list2[0])
    elif months.index(list1[1]) < months.index(list2[1]):
        print(list1[0])
    else:
        if int(list1[2]) < int(list2[2]):
            print(list1[0])
        elif int(list1[2]) > int(list2[2]):
            print(list2[0])
        else:
            print(list1[0],list2[0])




