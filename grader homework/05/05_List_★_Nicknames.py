n = int(input())
a = []
for i in range(n):
    name = input()
    a.append(name)
nickname = ['Dick','Bill','Jim','Jack','Peggy','Ed','Sally','Andy','Tony','Debbie']
first = ['Robert','William','James','John','Margaret','Edward','Sarah','Andrew','Anthony','Deborah']
for i in range(len(a)):
    if a[i] in first:
        print(nickname[first.index(a[i])])
    elif a[i] in nickname:
        print(first[nickname.index(a[i])])
    else:
        print('Not found')