a = input()
b = []
for i in a:
    if i not in '.,;:[]-=()\\\'\"><':
        b.append(i)
    else:
        b.append(' ')
temp = ''
temp = ''.join(b).split()
up = []
for i in range(len(temp)):
    temp[i] = temp[i].lower()
    up.append(temp[i][0])
for i in range(1,len(up)):
    up[i] = up[i].upper()
for i in range(len(up)):
    for j in range(1,len(temp[i])):
        up[i] = up[i] + temp[i][j]
final = ''.join(up)
print(final)