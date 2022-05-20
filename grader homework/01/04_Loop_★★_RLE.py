n = input()
n = list(n)
k = []
ch = n[0]
count = 0
for i in range(len(n)):
    if n[i] == ch:
        count = count + 1
    else:
        k.append([ch,count])
        ch = n[i]
        count = 1
k.append([ch,count])
final = ''
for i in range(len(k)):
    for j in k[i]:
        final = final + str(j) + ' '
print(final)