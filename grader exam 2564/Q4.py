r,c = [int(e) for e in input().split()]
l = []
for i in range(r):
    temp = [e for e in input()]
    l.append(temp)
want = [e for e in input()]
ch = []
for i in range(len(want)):
    templ = []
    for j in range(len(l)):
        for k in range(len(l[0])):
            if want[i] == l[j][k]:
                templ.append((j,k))
    ch.append(templ)

finding = True
chosen = []
i = 0

while i < len(ch[0]):
    if i < 0:
        i = 0
    b = []
    b.append(ch[0][i])
    j = 1
    while finding:
        t = 0
        for k in range(len(ch[j])):
            dx = b[-1][1] - ch[j][k][1]
            dy = b[-1][0] - ch[j][k][0]
            if abs(dx) + abs(dy) == 1 and ch[j][k] not in b:
                b.append(ch[j][k])
                i += 1
                break
            else:
                t += 1
            if t == len(ch[j]):
                k = b[-1]
                b.remove(k)
                ch[j-1].remove(k)
                j = j-2
        if j == len(want)-1:
            break
        elif len(b) == 0:
            j += 1
            break
        j += 1
    if len(b) != len(want):
        b = []
        i -= 1
        continue
    else:
        chosen.append(b)
        break
print(chosen[0])
            
        