n = int(input())
d = {}
d1 = {}
for i in range(n):
    name = input().split()
    d[name[0]] = name[1]
    d1[name[1]] = name[0]
m = int(input())
for i in range(m):
    k = input()
    if k in d:
        print(d[k])
    elif k in d1:
        print(d1[k])
    else:
        print('Not found')