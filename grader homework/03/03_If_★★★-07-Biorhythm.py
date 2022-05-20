import math
bd,bm,by,d,m,y = [int(e) for e in input().split()] #list
by = by-543
y = y-543
list1 = [31,28,31,30,31,30,31,31,30,31,30,31]
list2 = [31,29,31,30,31,30,31,31,30,31,30,31]
t1 = 0
t2 = 0
total = 0
if (by % 4 == 0 and by%100 != 0) or by%400==0:
    for i in range(len(list2)):
        if bm - 1 == i:
            t1 = list2[i] - bd + 1
    for j in range(bm,len(list2)):
        t1 = t1 + list2[j]
else:
    for i in range(len(list1)):
        if bm - 1 == i:
            t1 = list1[i] - bd + 1
    for j in range(bm,len(list1)): #10->12
        t1 = t1 + list1[j]
if (y % 4 == 0 and y%100 != 0) or y%400==0:
    for i in range(0,m-1):
        total = total + list2[i]
    t2 = total + d - 1 
else:
    for i in range(0,m-1):
        total = total + list1[i]
    t2 = total + d -1
dt = y - by -1
t3 = dt*365
t = t1 + t2 + t3
p_rad = math.radians((360*(t))/23)
e_rad = math.radians((360*(t))/28)
i_rad = math.radians((360*(t))/33)
x = math.sin((p_rad))
y = math.sin((e_rad))
z = math.sin((i_rad))
print(t,"{:.2f}".format(x),"{:.2f}".format(y),"{:.2f}".format(z) )
