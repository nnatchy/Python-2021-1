n = int(input())
a = []
a.append(n)
while n != 1:
    if n%2 == 0:
        n = n//2
    else:
        n = 3*n + 1
    a.append(n)
if len(a) > 15:
    for i in range(len(a)-15):
        a.pop(0)
final = ''
for i in a:
    final = final + str(i) + '->'
final = final[0:len(final)-2]
print((final))

