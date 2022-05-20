d = {}
for i in range(int(input())):
    info = input().split()
    d[info[0]] = info[1:]
wanted = set(input().split())
final = []
for key in d:
    if wanted.issubset(d[key]):
        final.append([key,d[key]])
if len(final) == 0:
    print('Not Found')
else:
    final.sort()
    for i in range(len(final)):
        print('%s %s' %(final[i][0],' '.join(final[i][1])))
