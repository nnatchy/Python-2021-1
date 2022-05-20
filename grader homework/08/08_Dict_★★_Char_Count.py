import string
name = input().strip().lower()
d = {}
for i in name:
    if i in d:
        d[i] += 1
    elif i not in string.ascii_lowercase:
        continue
    else:
        d[i] = 1
l = []
for i in d:
    l.append([-int(d[i]),i])
l.sort()
for i in range(len(l)):
    print(l[i][1],'->',-l[i][0])

