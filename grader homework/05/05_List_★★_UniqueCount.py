a = input().split()
ch = a[0]
b = []
b.append(ch)
count = 1
for i in range(len(a)):
    if a[i] != ch:
        b.append(a[i])
    else:
        ch = a[i]
for i in range(len(b)):
    b[i] = int(b[i])
b.sort()
k = b[0]
c = []
c.append(k)
for i in range(len(b)):
    if k != b[i]:
        c.append(b[i])
        k = b[i]
        count += 1
d = []
if len(c) > 10:
    for i in range(10):
        d.append(c[i])
    print(count)
    print(d)
else:
    for i in range(len(c)):
        d.append(c[i])
    print(count)
    print(d)