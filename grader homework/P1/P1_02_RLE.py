a = input()
l = []
if a == 'str2RLE':
    b = input()
    l = []
    count = 0
    q = b[0]
    for i in b:
        if q == i:
            count += 1
        else:
            l.append([q,count])
            q = i
            count = 1
    l.append([q,count])
    final = ''
    for i in range(len(l)):
        for j in l[i]:
            final = final + str(j) + ' '
    print(final)
elif a == 'RLE2str':
    b = input().split(' ')
    final = ''
    for i in range(0,len(b),2):
        final = final + b[i] * int(b[i+1])
    print(final)
else:
    print('Error')


    