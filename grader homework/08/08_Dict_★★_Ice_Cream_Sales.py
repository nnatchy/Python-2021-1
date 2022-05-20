n = int(input())
d = {}
for i in range(n):
    product,price = input().split()
    d[product] = float(price)
d1 = {}
m = int(input())
for i in range(m):
    product,amount = input().split()
    if product in d1:
        d1[product] += int(amount)
    else:
        d1[product] = int(amount)
for key in d1:
    if key in d:
       d1[key] *= int(d[key])
    else:
        pass
total = 0
temp = 0
l = []
val = []
for key in d1:
    if key in d:
        temp += d1[key]
        l.append([temp,key])
        val.append(temp)
        total += temp
        temp = 0
l.sort()
name = []
if total == 0:
    print('No ice cream sales')
else:
    print('Total ice cream sales: %s' %(float(total)))
    for i in range(len(l)):
        if l[i][0] == max(val):
            name.append(l[i][1])
    b = ', '.join(name)
    print('Top sales:',b)
            
        



    


