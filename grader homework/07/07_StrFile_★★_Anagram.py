a = input()
a = a.lower()
b = input()
b = b.lower()
l1 = []
l2 = []
for i in a:
    if i in ' ':
        pass
    else:
        l1.append(i)
for i in b:
    if i in ' ':
        pass
    else:
        l2.append(i)
l1.sort()
l2.sort()
if l1 == l2:
    print('YES')
else:
    print('NO')