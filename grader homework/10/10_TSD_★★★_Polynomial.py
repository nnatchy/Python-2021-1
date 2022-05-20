def add_poly(p1, p2):
    final = p1+p2
    l = []
    for i in range(len(final)):
        l.append([final[i][0], final[i][1]])
    d = {}
    order = []
    for val, key in l:
        if key in d:
            d[key] += val
        else:
            d[key] = val
            order.append(key)
    fin = []
    d1 = {}
    for key in d:
        if d[key] != 0:
            d1[key] = d[key]
    lf = []
    for i in order:
        if i in d1:
            lf.append(i)
    finals = []
    lf.sort()
    for key in lf[::-1]:
        finals.append((d1[key],key))
    return finals

def mult_poly(p1, p2):
    l = []
    for i in range(len(p1)):
        for j in range(len(p2)):
            l.append([p1[i][0]*p2[j][0], p1[i][1]+p2[j][1]])
    d = {}
    order = []
    for val, key in l:
        if key in d:
            d[key] += val
        else:
            d[key] = val
            order.append(key)
    fin = []
    d1 = {}
    for key in d:
        if d[key] != 0:
            d1[key] = d[key]
    lf = []
    for i in order:
        if i in d1:
            lf.append(i)
    finals = []
    lf.sort()
    for key in lf[::-1]:
        finals.append((d1[key],key))
    return finals

for i in range(3):
    exec(input().strip())
