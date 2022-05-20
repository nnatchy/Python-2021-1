n = int(input())
k = int(input())
if (n < 1 or n%1 != 0) and (k < 1):
    print('Invalid n and k')
elif n < 1 or n %1 != 0:
    print('Invalid n')
elif k < 1:
    print('Invalid k')
else:   
    out = ''
    s = ''
    for i in range(1, k+1):
        if i <= k-1:
            t = str(i)
            while len(t) < n+1:
                t += '-'
            s += t
        else:
            t = str(i)
            while len(t) < n:
                t += '-'
            s += t
    print(s)

    l = ['0','1']
    while len(l[0]) < n:
        for i in reversed(l):
            l.append(i)
        for i in range(len(l)):
            if i < len(l)//2:
                l[i] = '0' + l[i]
            else:
                l[i] = '1' + l[i]
    b = []
    d = 0
    for i in range(2**n//k):
        a = []
        for j in range(k):
            if d < len(l):
                a.append(l[d])
            else:
                break
            d += 1
        b.append(a)
    if 2**n%k != 0:
        temp = []
        for i in range((2**n)-2**n%k,2**n):
            temp.append(l[i])
        b.append(temp)
    for i in range(len(b)):
        print(','.join(b[i]))
