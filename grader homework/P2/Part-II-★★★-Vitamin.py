def appendprice(n,l):
    price = []
    for i in range(len(l)):
        price.append(float(l[i][int(n)]))
    return price

n = int(input())
l = []
for i in range(n):
    fruit = input().split()
    l.append(fruit)
q = input().split()
if q[0] == 'show':
    for i in range(len(l)):
        print(' '.join(l[i]))
elif q[0] == 'get':
    p = []
    for i in range(len(l)):
        if q[1] in l[i] :
            print(' '.join(l[i]))
            p.append(l[i])
    if len(p) == 0:
        print('%s not found'%(q[1]))
elif q[0] == 'avg':
    price = appendprice((q[1]),l)
    print(round(sum(price)/n,4))
elif q[0] == 'max':
    p = []
    for i in range(len(l)):
        p.append([l[i][int(q[1])],l[i][0]])
    p.sort()
    p = p[::-1]
    ma = p[0][0]
    k = []
    for i in p:
        if ma in i:
            k.append(i)
    print(k[-1][1],k[-1][0])
elif q[0] == 'sort':
    sort = []
    for i in range(len(l)):
        sort.append([l[i][int(q[1])],l[i][0]])
    sort.sort()
    st1 = ''
    for i in range(len(sort)):
        st1 += sort[i][1] + ' '
    print(st1[:-1])