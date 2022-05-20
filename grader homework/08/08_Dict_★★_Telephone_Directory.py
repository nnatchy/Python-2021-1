n = int(input())
d = {}
d1 = {}
for i in range(n):
    name,surname,tel = input().split()
    realName = name + ' '+surname
    d[realName] = tel
    d1[tel] = realName
l = []
for i in range(int(input())):
    stuff = input()
    l.append(stuff)
for stuff in l:
    #for key in d:
    if stuff in d:
        print(stuff,'-->',d[stuff])  
    elif stuff in d1:
        print(stuff,'-->',d1[stuff])
    else:
        print(stuff,'-->','Not found')