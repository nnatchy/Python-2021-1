d = {}
ids = []
for i in range(int(input())):
    zone = [e for e in input().split(': ')]
    ids.append(zone[0])
    city = zone[1].split(', ')
    for i in range(len(city)):
        city[i] = city[i][0]
    d[zone[0]] = set(city)
a = input()
final = []
lookZone = d[a]
for id,zone in d.items():
    if len(zone.intersection(lookZone)) > 0 and id != a:
        final.append(id)
if len(final) == 0:
    print('Not Found')
else:
    for i in ids:
        if i in final:
            print(i)