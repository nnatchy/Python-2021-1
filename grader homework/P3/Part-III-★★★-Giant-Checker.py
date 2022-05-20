import string
lower = string.ascii_lowercase
row = {}
a = 1
for i in range(1,53):
    row[i] = a
    a += 1
col = {}
a = 1
for i in range(len(lower)):
    col[lower[i]] = a
    a += 1
fposition = input().strip()
l = []
num = []
for i in range(1,53):
    num.append(str(i))
    num.append(i)
if 'row' not in fposition:
    position = ''
    for i in fposition:
        if i!=' ':
            position += i
    if position[0] not in string.ascii_letters and (position[1:] not in num):
        print('Invalid row and column')
    elif position[0] not in string.ascii_letters:
        print('Invalid row')
    elif position[1:] == '':
        print('Invalid column')
    elif int(position[1:]) > 52 or int(position[1:]) not in num:
        print('Invalid column')
    else:
        for i in (position):
            if i in string.ascii_letters or i in num:
                l.append(i.lower())
        if len(l) == 3:
            data = col[l[0]] + row[int(l[1]+l[2])]
            if data%2 != 0:
                print('Black')
            else:
                print('White')
        else:
            data = col[l[0]] + row[int(l[1])]
            if data%2 != 0:
                print('Black')
            else:
                print('White')
else:
    l1 = fposition.split(',')
    temp = []
    for i in range(len(l1)):
        index = l1[i].find('=')
        temp.append(l1[i][index+1:].strip())
    if temp[0] in string.ascii_letters:
        if temp[0][:] not in col and (temp[1] not in num):
            print('Invalid row and column')
        elif temp[0] not in string.ascii_letters:
            print('Invalid row')
        elif temp[1] not in num:
            print('Invalid column')
        else:
            if temp[0] in string.ascii_letters:
                data = col[temp[0].lower()] + row[int(temp[1])]
                if data%2 != 0:
                    print('Black')
                else:
                    print('White')
            else:
                data = col[temp[1]] + row[int(temp[0])]
                if data%2 != 0:
                    print('Black')
                else:
                    print('White')
    elif temp[0] in num:
        if temp[1] not in string.ascii_letters and (temp[0] not in num):
            print('Invalid row and column')
        elif temp[1] not in string.ascii_letters:
            print('Invalid row')
        elif temp[0] not in num:
            print('Invalid column')
        else:
            if temp[0] in string.ascii_letters:
                data = col[temp[0].lower()] + row[int(temp[1])]
                if data%2 != 0:
                    print('Black')
                else:
                    print('White')
            else:
                data = col[temp[1].lower()] + row[int(temp[0])]
                if data%2 != 0:
                    print('Black')
                else:
                    print('White')
    else:
        print('Invalid column')