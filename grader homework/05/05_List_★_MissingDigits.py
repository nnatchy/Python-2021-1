a = input()
b = []
for i in range(10):
    if str(i) not in a:
        b.append(i)
for i in range(len(b)):
    b[i] = str(b[i])
b = ','.join(b)
if len(b) == 0:
    print('None')
else:
    print(b)
