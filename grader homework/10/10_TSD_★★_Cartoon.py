name = [i.strip() for i in input().split(',')]
d = {}
order = []
while name != ['q']:
    if name[1] not in d:
        d[name[1]] = name[0]+', '
        order.append(name[1])
    else:
        d[name[1]] += name[0]+', '
    name = [i.strip() for i in input().split(',')]
for key in d:
    d[key] = d[key][:-2]
for i in order:
    print('%s: %s' %(i,d[i]))