a = input()
b = input()
count = 0
if len(a) != len(b):
    print('Incomplete answer')
else:
    for i in range(len(a)):
        if b[i] == a[i]:
            count += 1
    print(count)