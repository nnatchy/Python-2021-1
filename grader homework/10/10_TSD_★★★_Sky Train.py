station = []
inp = input().split()
station.append(inp)
while len(inp) == 2:
    inp = input().split()
    station.append(inp)
wanted = station.pop(-1)[0]
statecango = []
statecango.append(wanted)
for i in range(len(station)):
    if wanted in station[i]:
        station[i].remove(wanted)
        statecango.append(station[i][0])
l = []
for i in range(len(station)):
    if len(station[i]) > 1:
        for j in statecango:
            if j in station[i] and len(station[i]) > 1:
                station[i].remove(j)
                l.append(station[i][0])
for i in range(len(l)):
    statecango.append(l[i])
statecango.sort()
order = []
ss = set(statecango)
for i in ss:
    order.append(i)
for i in sorted(order):
    print(i)

        




