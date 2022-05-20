a = input()
b = input()
c = []
count = 0
for i in b:
    if i in '".,=()[]' or i in "'":
        c.append(' ')
    else:
        c.append(i)
d = ''
for i in range(len(c)):
    d = d + c[i]
final = (d.split(' '))
for i in range (len(final)):
    if a == final[i]:
        count += 1
print(count)