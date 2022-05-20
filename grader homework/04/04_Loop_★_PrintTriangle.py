h = int(input())
for i in range(h):
    for j in range(h-i-2,-1,-1):
        print(' ',end='')
    for k in range(i+1):
        if k == 0: #k = 0
            print('*',end='')
        elif i == h-1:
            print('*',end='')
        else:
            print(' ',end='')
    for k in range(i):
        if k+1 == i: #k = 6
            print('*',end='')
        elif i == h-1:
            print('*',end='')
        else:
            print(' ',end='')
    print('')
