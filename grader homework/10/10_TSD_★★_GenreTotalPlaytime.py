d = {}
for i in range(int(input())):
    name,singer,genre,time = input().split(', ')
    minu,sec = [int(i) for i in time.split(':')]
    genre.strip()
    if genre not in d:
        d[genre] = (minu*60) + sec
    else:
        d[genre] += (minu*60) + sec
l = []
for key,time in d.items():
    l.append([time,key])
l.sort();l = l[::-1]
for i in range(len(l)):
    if l[i][0]%60 < 10:
        l[i][0] = str(l[i][0]//60)+':'+'0'+str((l[i][0]%60))
    else:
        l[i][0] = str(l[i][0]//60)+':'+str((l[i][0]%60))
if len(l) >= 3:
    for i in range(3):
        print('%s --> %s' %(l[i][1],l[i][0]))
else:
    for i in range(len(l)):
        print('%s --> %s' %(l[i][1],l[i][0]))