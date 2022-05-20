a,b,c,d = [float(i) for i in input().split()]
list1 = [a,b,c,d]
total = 0
max_ = 0
min_ = 0
for i in range(len(list1)):
    if i == 0:
        max_ = list1[i]
    else:
        if list1[i] > max_:
            max_ = list1[i]
for k in range(len(list1)):
    if k == 0:
        min_ = list1[k]
    else:
        if list1[k] < min_:
            min_ = list1[k]
list1.remove(max_)
list1.remove(min_)
for i in range(len(list1)):
    total += list1[i]
print(round(total/len(list1),2))
