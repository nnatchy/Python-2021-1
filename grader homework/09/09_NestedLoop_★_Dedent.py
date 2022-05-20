import string
l = []
for i in range(int(input())):
    line = input()
    l.append(line)
for i in range(len(l)):
    count = 0
    for j in l[i]:
        if j == '.':
            count += 1
        elif j in string.ascii_lowercase or j in '0123456789':
            break
    temp = ''
    if l[i] == '':
        print(l[i])
    elif l[i][0] == '.':
        for j in range(count//2, len(l[i])):
            temp = temp + l[i][j]
    else:
        for j in range(len(l[i])):
            temp = temp + l[i][j]
    l[i] = temp
    print(l[i])
