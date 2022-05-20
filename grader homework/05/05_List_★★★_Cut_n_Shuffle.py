a = input().split()
b = input()
l = []
for i in range(len(b)):
    l.append(b[i])
for i in l:
    if i == 'C':
        a = a[len(a)//2:] + a[:len(a)//2]
    elif i == 'S':
        l1 = [0]*len(a)
        l1[1::2] = a[len(a)//2:]
        l1[0::2] = a[:len(a)//2]
        a = l1
final = ' '.join(a)
print(final)
