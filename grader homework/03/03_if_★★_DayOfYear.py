a = int(input())
b = int(input())
c = int(input())
d = c-543
total = 0
sum_ = 0
list1 = [0,31,59,90,120,151,181,212,243,273,304,334]
list2 = [0,31,60,91,121,152,182,213,244,274,305,335]
if (d%4 == 0 and d%100 != 0) or d%400==0:
    for k in range(len(list2)):
        if b-1 == k:
            total = list2[k] + a
            print(total)
else:
    for i in range(len(list1)):
        if b-1 == i:
            sum_ = list1[i] + a
            print(sum_)